DROP TABLE IF EXISTS #DateText;
-- Create the temporary table
SELECT DateKey AS DateText 
INTO #DateText
FROM Calendar;

ALTER TABLE #DateText
ALTER COLUMN DateText
nvarchar(255);

SELECT c.name AS COLUMN_NAME, 
       t.name AS DATA_TYPE
FROM tempdb.sys.columns c
JOIN tempdb.sys.types t ON c.user_type_id = t.user_type_id
WHERE c.object_id = OBJECT_ID('tempdb..#DateText');

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