-- Use two functions to query the system's local date, without timezone information. Show the dates in different formats.
SELECT 
	CONVERT(VARCHAR(24), SYSDATETIME(), 107) AS HighPrecision,
	CONVERT(VARCHAR(24), SYSDATETIME(), 102) AS LowPrecision;

-- Use two functions to retrieve the current time, in Universal Time Coordinate.
SELECT 
	CAST(SYSUTCDATETIME() AS time) AS HighPrecision,
	CAST(SYSUTCDATETIME() AS time) AS LowPrecision;