import pyodbc
import pandas as pd

DB_PARAMS = (
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=datacamp;"
    "Trusted_Connection=True;"
)

try:
    conn = pyodbc.connect(DB_PARAMS)
    cursor = conn.cursor()
    
    sql_script = """
    IF OBJECT_ID('dbo.Calendar', 'U') IS NOT NULL
        DROP TABLE dbo.Calendar;
    
    CREATE TABLE Calendar (
        DateKey INT PRIMARY KEY,
        Date DATE NOT NULL,
        Day INT NOT NULL,
        DayOfWeek INT NOT NULL,
        DayName VARCHAR(10) NOT NULL,
        IsWeekend BIT NOT NULL,
        DayOfWeekInMonth INT NOT NULL,
        CalendarDayOfYear INT NOT NULL,
        WeekOfMonth INT NOT NULL,
        CalendarWeekOfYear INT NOT NULL,
        CalendarMonth INT NOT NULL,
        MonthName VARCHAR(10) NOT NULL,
        CalendarQuarter INT NOT NULL,
        CalendarQuarterName VARCHAR(2) NOT NULL,
        CalendarYear INT NOT NULL,
        FirstDayOfMonth DATE NOT NULL,
        LastDayOfMonth DATE NOT NULL,
        FirstDayOfWeek DATE NOT NULL,
        LastDayOfWeek DATE NOT NULL,
        FirstDayOfQuarter DATE NOT NULL,
        LastDayOfQuarter DATE NOT NULL,
        CalendarFirstDayOfYear DATE NOT NULL,
        CalendarLastDayOfYear DATE NOT NULL,
        FirstDayOfNextMonth DATE NOT NULL,
        CalendarFirstDayOfNextYear DATE NOT NULL,
        FiscalDayOfYear INT NOT NULL,
        FiscalWeekOfYear INT NOT NULL,
        FiscalMonth INT NOT NULL,
        FiscalQuarter INT NOT NULL,
        FiscalQuarterName VARCHAR(2) NOT NULL,
        FiscalYear INT NOT NULL,
        FiscalFirstDayOfYear DATE NOT NULL,
        FiscalLastDayOfYear DATE NOT NULL,
        FiscalFirstDayOfNextYear DATE NOT NULL
    );

    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\04_Course_Time_Series_Analysis_in_SQL_Server\\datasets\\CalendarTable.csv"
    df = pd.read_csv(file_path)
    
    # Insert data into SQL Server
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.Calendar(DateKey,Date,Day,DayOfWeek,DayName,IsWeekend,DayOfWeekInMonth,CalendarDayOfYear,WeekOfMonth,CalendarWeekOfYear,CalendarMonth,MonthName,CalendarQuarter,CalendarQuarterName,CalendarYear,FirstDayOfMonth,LastDayOfMonth,FirstDayOfWeek,LastDayOfWeek,FirstDayOfQuarter,LastDayOfQuarter,CalendarFirstDayOfYear,CalendarLastDayOfYear,FirstDayOfNextMonth,CalendarFirstDayOfNextYear,FiscalDayOfYear,FiscalWeekOfYear,FiscalMonth,FiscalQuarter,FiscalQuarterName,FiscalYear,FiscalFirstDayOfYear,FiscalLastDayOfYear,FiscalFirstDayOfNextYear)VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            row["DateKey"], row["Date"], row["Day"], row["DayOfWeek"], row["DayName"], row["IsWeekend"], row["DayOfWeekInMonth"], row["CalendarDayOfYear"], row["WeekOfMonth"], row["CalendarWeekOfYear"], row["CalendarMonth"], row["MonthName"], row["CalendarQuarter"], row["CalendarQuarterName"], row["CalendarYear"], row["FirstDayOfMonth"], row["LastDayOfMonth"], row["FirstDayOfWeek"], row["LastDayOfWeek"], row["FirstDayOfQuarter"], row["LastDayOfQuarter"], row["CalendarFirstDayOfYear"], row["CalendarLastDayOfYear"], row["FirstDayOfNextMonth"], row["CalendarFirstDayOfNextYear"], row["FiscalDayOfYear"], row["FiscalWeekOfYear"], row["FiscalMonth"], row["FiscalQuarter"], row["FiscalQuarterName"], row["FiscalYear"], row["FiscalFirstDayOfYear"], row["FiscalLastDayOfYear"], row["FiscalFirstDayOfNextYear"]
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.Calendar;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'Calendar' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")