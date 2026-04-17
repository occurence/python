SELECT 
  TrackId,
  name AS track_name,
  title AS album_title
FROM track
  -- Complete the join type and the common joining column
INNER JOIN album on track.AlbumId = album.AlbumId;

-- Select album_id and title from album, and name from artist
SELECT 
  AlbumId,
  title,
  name AS artist
  -- Enter the main source table name
FROM artist
  -- Perform the inner join
INNER JOIN album on artist.ArtistId = album.ArtistId;

SELECT TrackId,
-- Enter the correct table name prefix when retrieving the name column from the track table
  track.name AS track_name,
  title as album_title,
  -- Enter the correct table name prefix when retrieving the name column from the artist table
  artist.name AS artist_name
FROM track
  -- Complete the matching columns to join album with track, and artist with album
INNER JOIN album on track.AlbumId = album.AlbumId 
INNER JOIN artist on album.ArtistId = artist.ArtistId;