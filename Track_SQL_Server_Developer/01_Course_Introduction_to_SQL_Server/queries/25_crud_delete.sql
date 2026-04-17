-- Run the query
SELECT 
  * 
FROM 
  album
ORDER BY
  AlbumId DESC;
-- DELETE the record
DELETE FROM 
  album 
WHERE 
  AlbumId = 1000
-- Run the query again
SELECT 
  * 
FROM 
  album
ORDER BY
  AlbumId DESC;
-- Complete the statement to enter the data to the table         
INSERT INTO album
-- Specify the destination columns
(AlbumId, Title, ArtistId)
-- Insert the appropriate values for album id, title and artist id
VALUES
  (1000, 'For Those About To Rock We Salute You', 1);
-- Run the query again
SELECT 
  * 
FROM 
  album
WHERE
  AlbumId = 1000