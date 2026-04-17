-- Change the language, so that '30.03.2019' is considered a valid date. Select the name of the month.
DECLARE @date1 NVARCHAR(20) = '30.03.2019';

-- Set the correct language
SET LANGUAGE Dutch;
SELECT
	@date1 AS initial_date,
    -- Check that the date is valid
	ISDATE(@date1) AS is_valid,
    -- Select the name of the month
	DATENAME(MONTH, @date1) AS month_name;