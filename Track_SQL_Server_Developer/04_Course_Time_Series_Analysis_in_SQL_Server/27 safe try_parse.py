import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
"""
# cursor.execute(variable_query)
# conn.commit()

select_query = """
DECLARE
	@GoodDateINTL NVARCHAR(30) = '2019-03-01 18:23:27.920',
	@GoodDateDE NVARCHAR(30) = '13.4.2019',
	@GoodDateUS NVARCHAR(30) = '4/13/2019',
	@BadDate NVARCHAR(30) = N'SOME BAD DATE';

-- -- The prior solution using TRY_CAST
-- SELECT
-- 	TRY_CAST(@GoodDateINTL AS DATETIME2(3)) AS GoodDateINTL,
-- 	TRY_CAST(@GoodDateDE AS DATE) AS GoodDateDE,
-- 	TRY_CAST(@GoodDateUS AS DATE) AS GoodDateUS,
-- 	TRY_CAST(@BadDate AS DATETIME2(3)) AS BadDate;

SELECT
	TRY_PARSE(@GoodDateINTL AS DATETIME2(3)) AS GoodDateINTL,
    -- Fill in the correct region based on our input
    -- Be sure to match these data types with the
    -- TRY_CAST() examples above!
	TRY_PARSE(@GoodDateDE AS DATE USING 'de-de') AS GoodDateDE,
	TRY_PARSE(@GoodDateUS AS DATE USING 'en-us') AS GoodDateUS,
    -- TRY_PARSE can't fix completely invalid dates
	TRY_PARSE(@BadDate AS DATETIME2(3) USING 'sk-sk') AS BadDate;
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()