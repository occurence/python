DECLARE @date1 NVARCHAR(20) = '2018-30-12';

-- Set the date format and check if the variable is a date
SET DATEFORMAT 'ydm';
SELECT ISDATE(@date1) AS result;