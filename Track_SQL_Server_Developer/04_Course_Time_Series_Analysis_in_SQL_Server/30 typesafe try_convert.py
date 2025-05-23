import pyodbc
import pandas as pd

conn = pyodbc.connect( "DRIVER={SQL Server};" "SERVER=Arc-PC;" "DATABASE=datacamp;" "Trusted_Connection=True;" )
cursor = conn.cursor()

variable_query = """
DROP TABLE IF EXISTS #DateText;
-- Create the temporary table
SELECT DateKey AS DateText 
INTO #DateText
FROM Calendar;

-- Insert data into the temporary table
-- INSERT INTO #DateText (DateText) VALUES
-- (N'20060210'), (N'20060211'), (N'20060212'), (N'20060213'), (N'20060214'), (N'20060215'), (N'20060216'), (N'20060217'), (N'20060218'), (N'20060219'), (N'20060220'), (N'20060221'), (N'20060222'), (N'20060223'), (N'20060224'), (N'20060225'), (N'20060226'), (N'20060227'), (N'20060228'), (N'20060301'), (N'20060302'), (N'20060303'), (N'20060304'), (N'20060305'), (N'20060306'), (N'20060307'), (N'20060308'), (N'20060309'), (N'20060310'), (N'20060311'), (N'20060312'), (N'20060313'), (N'20060314'), (N'20060315'), (N'20060316'), (N'20060317'), (N'20060318'), (N'20060319'), (N'20060320'), (N'20060321'), (N'20060322'), (N'20060323'), (N'20060324'), (N'20060325'), (N'20060326'), (N'20060327'), (N'20060328'), (N'20060329'), (N'20060330'), (N'20060331'), (N'20060401'), (N'20060402'), (N'20060403'), (N'20060404'), (N'20060405'), (N'20060406'), (N'20060407'), (N'20060408'), (N'20060409'), (N'20060410'), (N'20060411'), (N'20060412'), (N'20060413'), (N'20060414'), (N'20060415'), (N'20060416'), (N'20060417'), (N'20060418'), (N'20060419'), (N'20060420'), (N'20060421'), (N'20060422'), (N'20060423'), (N'20060424'), (N'20060425'), (N'20060426'), (N'20060427'), (N'20060428'), (N'20060429'), (N'20060430'), (N'20060501'), (N'20060502'), (N'20060503'), (N'20060504'), (N'20060505'), (N'20060506'), (N'20060507'), (N'20060508'), (N'20060509'), (N'20060510'), (N'20060511'), (N'20060512'), (N'20060513'), (N'20060514'), (N'20060515'), (N'20060516'), (N'20060517'), (N'20060518'), (N'20060519'), (N'20060520');

ALTER TABLE #DateText
ALTER COLUMN DateText
nvarchar(255);
"""
cursor.execute(variable_query)
conn.commit()

select_query = """
-- Verify inserted data
-- SELECT * FROM #DateText;

-- Try out how fast the TRY_CONVERT() function is
-- by try-converting each DateText value to DATE
DECLARE @StartTimeConvert DATETIME2(7) = SYSUTCDATETIME();
SELECT TRY_CONVERT(DATE, DateText) AS TestDate FROM #DateText;
DECLARE @EndTimeConvert DATETIME2(7) = SYSUTCDATETIME();

-- Determine how much time the conversion took by
-- calculating the difference from start time to end time
SELECT
    DATEDIFF(MILLISECOND, @StartTimeConvert, @EndTimeConvert) AS ExecutionTimeConvert;
"""

df = pd.read_sql(select_query, conn)
print(df)
cursor.close()
conn.close()