-- Select the album
SELECT 
  title 
FROM 
  album 
WHERE 
  AlbumId = 213;
-- UPDATE the title of the album
UPDATE 
  album 
SET 
  title = 'Pure Cult: The Best Of The Cult' 
WHERE 
  AlbumId = 213;
-- Run the query again
SELECT 
  title 
FROM 
  album
WHERE 
  AlbumId = 213;
-- UPDATE the title of the album
UPDATE 
  album 
SET 
  title = 'Pure Cult: The Best Of The Cult (For Rockers Ravers Lovers & Sinners) UK' 
WHERE 
  AlbumId = 213;
-- Run the query again
SELECT 
  title 
FROM 
  album
WHERE 
  AlbumId = 213;