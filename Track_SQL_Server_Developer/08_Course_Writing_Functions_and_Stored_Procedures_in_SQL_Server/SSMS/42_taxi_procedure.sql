-- Create the stored procedure
CREATE PROCEDURE dbo.cuspPickupZoneShiftStats
	-- Specify @Borough parameter
	@Borough nvarchar(30)
AS
BEGIN
SELECT
	DATENAME(WEEKDAY, PickupDate) as 'Weekday',
    -- Calculate the shift number
	dbo.GetShiftNumber(DATEPART(HOUR, PickupDate)) as 'Shift',
	Zone.Zone as 'Zone',
	FORMAT(AVG(dbo.ConvertDollar(TotalAmount, .77)/dbo.ConvertMiletoKM(TripDistance)), 'c', 'de-de') AS 'AvgFarePerKM',
	FORMAT(COUNT (ID),'n', 'de-de') as 'RideCount',
	FORMAT(SUM(DATEDIFF(SECOND, PickupDate, DropOffDate))/60, 'n', 'de-de') as 'TotalRideMin'
FROM YellowTripData
INNER JOIN TaxiZoneLookup as Zone on PULocationID = Zone.LocationID 
WHERE
	dbo.ConvertMiletoKM(TripDistance) > 0 AND
	Zone.Borough = @Borough
GROUP BY
	DATENAME(WEEKDAY, PickupDate),
    -- Group by shift
	dbo.GetShiftNumber(DATEPART(HOUR, PickupDate)),  
	Zone.Zone
ORDER BY CASE WHEN DATENAME(WEEKDAY, PickupDate) = 'Monday' THEN 1
              WHEN DATENAME(WEEKDAY, PickupDate) = 'Tuesday' THEN 2
              WHEN DATENAME(WEEKDAY, PickupDate) = 'Wednesday' THEN 3
              WHEN DATENAME(WEEKDAY, PickupDate) = 'Thursday' THEN 4
              WHEN DATENAME(WEEKDAY, PickupDate) = 'Friday' THEN 5
              WHEN DATENAME(WEEKDAY, PickupDate) = 'Saturday' THEN 6
              WHEN DATENAME(WEEKDAY, PickupDate) = 'Sunday' THEN 7 END,
         -- Order by shift
         dbo.GetShiftNumber(DATEPART(HOUR, PickupDate)),
         SUM(DATEDIFF(SECOND, PickupDate, DropOffDate))/60 DESC
END;

/*
SELECT 
    name, 
    type_desc, 
    OBJECT_DEFINITION(object_id) AS definition
FROM sys.objects
WHERE type IN ('P')
ORDER BY name;
*/