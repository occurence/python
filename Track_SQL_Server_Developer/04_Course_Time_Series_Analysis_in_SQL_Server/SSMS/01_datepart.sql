DECLARE
	@SomeTime DATETIME2(7) = SYSUTCDATETIME();

-- Retrieve the year, month, and day
SELECT
	DATEPART(YEAR, @SomeTime) AS TheYear,
	DATEPART(MONTH, @SomeTime) AS TheMonth,
	DATEPART(DAY, @SomeTime) AS TheDay;