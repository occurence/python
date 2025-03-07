DECLARE @date1 datetime = '2018-12-01';
DECLARE @date2 datetime = '2030-03-03';
SELECT DATEDIFF(YEAR, @date2 - @date1, @date1 + @date2)