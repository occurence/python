-- Calculate the average, minimum and maximum
SELECT AVG(DurationSeconds) AS Average, 
       MIN(DurationSeconds) AS Minimum, 
       MAX(DurationSeconds) AS Maximum
FROM Incidents

SELECT 
    AVG(DurationSeconds)::NUMERIC AS Average, 
    MIN(DurationSeconds)::NUMERIC AS Minimum, 
    MAX(DurationSeconds)::NUMERIC AS Maximum
FROM Incidents;

SELECT 
    TO_CHAR(AVG(DurationSeconds), '999999999999') AS Average, 
    TO_CHAR(MIN(DurationSeconds), '999999999999') AS Minimum, 
    TO_CHAR(MAX(DurationSeconds), '999999999999') AS Maximum
FROM Incidents;