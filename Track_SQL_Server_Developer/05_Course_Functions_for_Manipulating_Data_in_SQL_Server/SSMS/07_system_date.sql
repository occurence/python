-- Use the most common date function for retrieving the current date
SELECT 
	GETDATE() AS CurrentDate;

-- Select the current date in UTC time (Universal Time Coordinate) using two different functions.
SELECT 
	CURRENT_TIMESTAMP AS UTC_HighPrecision,
	GETUTCDATE() AS UTC_LowPrecision;

-- Select the local system's date, including the timezone information.
SELECT 
	SYSDATETIMEOFFSET() AS Timezone;