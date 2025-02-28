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

-- Try out how fast the TRY_PARSE() function is
-- by try-parsing each DateText value to DATE
DECLARE @StartTimeParse DATETIME2(7) = SYSUTCDATETIME();
SELECT TRY_PARSE(DateText AS DATE) AS TestDate FROM #DateText;
DECLARE @EndTimeParse DATETIME2(7) = SYSUTCDATETIME();

-- Determine how much time the conversion took by
-- calculating the difference from start time to end time
SELECT
    DATEDIFF(MILLISECOND, @StartTimeParse, @EndTimeParse) AS ExecutionTimeParse;