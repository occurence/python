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

-- Try out how fast the TRY_CAST() function is
-- by try-casting each DateText value to DATE
DECLARE @StartTimeCast DATETIME2(7) = SYSUTCDATETIME();
SELECT TRY_CAST(DateText AS DATE) AS TestDate FROM #DateText;
DECLARE @EndTimeCast DATETIME2(7) = SYSUTCDATETIME();

-- Determine how much time the conversion took by
-- calculating the date difference from @StartTimeCast to @EndTimeCast
SELECT
    DATEDIFF(MILLISECOND, @StartTimeCast, @EndTimeCast) AS ExecutionTimeCast;