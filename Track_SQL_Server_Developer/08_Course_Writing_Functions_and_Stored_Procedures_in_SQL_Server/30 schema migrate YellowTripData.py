import pyodbc
import pandas as pd

DB_PARAMS = (
    "DRIVER={SQL Server};"
    "SERVER=Arc-PC;"
    "DATABASE=DatabaseDesign;"
    "Trusted_Connection=True;"
)

try:
    conn = pyodbc.connect(DB_PARAMS)
    cursor = conn.cursor()
    
    sql_script = """
    IF OBJECT_ID('dbo.YellowTripData', 'U') IS NOT NULL
        DROP TABLE dbo.YellowTripData;
    
    CREATE TABLE YellowTripData (
        ID INT, 
        EmpNum char(10),
        PickupDate DATETIME2, 
        DropoffDate DATETIME2, 
        PassengerCount INT, 
        TripDistance FLOAT, 
        RateCodeID INT, 
        StoreFwdFlag CHAR(1), 
        PULocationID INT, 
        DOLocationID INT, 
        PaymentType INT, 
        FareAmount FLOAT, 
        FareExtra FLOAT, 
        MTATax FLOAT, 
        TipAmount FLOAT, 
        TollAmount FLOAT, 
        ImproveSurcharge FLOAT, 
        TotalAmount FLOAT
    );
    """
    
    cursor.execute(sql_script)
    conn.commit()
    
    # Load CSV into DataFrame
    file_path = r"D:\\STUDY\\python\\Track_SQL_Server_Developer\\08_Course_Writing_Functions_and_Stored_Procedures_in_SQL_Server\\datasets\\yellowtrip.csv"
    df = pd.read_csv(file_path)
    
    # Insert data into SQL Server~
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.YellowTripData(ID,EmpNum,PickupDate,DropoffDate,PassengerCount,TripDistance,RateCodeID,StoreFwdFlag,PULocationID,DOLocationID,PaymentType,FareAmount,FareExtra,MTATax,TipAmount,TollAmount,ImproveSurcharge,TotalAmount) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            row["ID"], row["EmpNum"], row["PickupDate"], row["DropoffDate"], row["PassengerCount"], row["TripDistance"], row["RateCodeID"], row["StoreFwdFlag"], row["PULocationID"], row["DOLocationID"], row["PaymentType"], row["FareAmount"], row["FareExtra"], row["MTATax"], row["TipAmount"], row["TollAmount"], row["ImproveSurcharge"], row["TotalAmount"]
        )
    
    conn.commit()
    
    # Retrieve and print data
    info_query = """
    SELECT * FROM dbo.YellowTripData;
    
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'YellowTripData' AND TABLE_SCHEMA = 'dbo';
    """
    
    cursor.execute(info_query)
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")