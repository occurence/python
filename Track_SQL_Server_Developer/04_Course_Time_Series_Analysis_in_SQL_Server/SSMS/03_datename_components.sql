DECLARE
	@BerlinWallFalls DATETIME2(7) = '1989-11-09 23:49:36.2294852';

-- Fill in the function to show the name of each date part
SELECT
	DATEPART(YEAR, @BerlinWallFalls) AS TheYear,
-- Fill in an additional function to extract names from date parts    
    DATENAME(MONTH, @BerlinWallFalls) AS MonthName,
    DATENAME(WEEKDAY, @BerlinWallFalls) AS DayOfWeek,
	DATEPART(DAYOFYEAR, @BerlinWallFalls) AS TheDayOfYear,
	DATEPART(DAY, @BerlinWallFalls) AS TheDay,
	DATEPART(WEEK, @BerlinWallFalls) AS TheWeek,
	DATEPART(SECOND, @BerlinWallFalls) AS TheSecond,
	DATEPART(NANOSECOND, @BerlinWallFalls) AS TheNanosecond;