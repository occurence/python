-- Set the correct date format so that the variable @date1 is interpreted as a valid date.
DECLARE @date1 NVARCHAR(20) = '15/2019/4';

-- Set the date format and check if the variable is a date
SET DATEFORMAT 'dym';
SELECT ISDATE(@date1) AS result;