DROP TABLE IF EXISTS #maxtracks;
SELECT album.title AS album_title,
  artist.name as artist,
  MAX(track.milliseconds / (1000 * 60) % 60 ) AS max_track_length_mins
-- Name the temp table #maxtracks
INTO #maxtracks
FROM album
-- Join album to artist using artist_id
INNER JOIN artist ON album.ArtistId = artist.ArtistId
-- Join track to album using album_id
INNER JOIN track ON album.AlbumId = track.AlbumId
GROUP BY artist.ArtistId, album.title, artist.name,album.AlbumId
-- Run the final SELECT query to retrieve the results from the temporary table
SELECT album_title, artist, max_track_length_mins
FROM  #maxtracks
ORDER BY max_track_length_mins DESC, artist;