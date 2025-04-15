-- Find the first day of the current month
SELECT DATEADD(MONTH, DATEDIFF(MONTH, 0, GETDATE()), 0)