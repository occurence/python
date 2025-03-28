-- Check the IncidentState column for missing values and replace them with the City column
-- SELECT IncidentState, ISNULL(IncidentState, City) AS Location
SELECT IncidentState, COALESCE(IncidentState, City) AS Location
FROM Incidents
-- Filter to only return missing values from IncidentState
WHERE IncidentState IS NULL