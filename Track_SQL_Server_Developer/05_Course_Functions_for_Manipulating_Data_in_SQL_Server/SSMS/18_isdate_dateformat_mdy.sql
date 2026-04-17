-- Set the correct date format so that the variable @date1 is interpreted as a valid date.
DECLARE @date1 NVARCHAR(20) = '10.13.2019';

-- Set the date format and check if the variable is a date
SET DATEFORMAT 'mdy';
SELECT ISDATE(@date1) AS result;