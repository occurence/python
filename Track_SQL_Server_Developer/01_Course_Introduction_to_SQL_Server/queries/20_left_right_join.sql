SELECT 
  InvoiceLineId,
  UnitPrice, 
  quantity,
  BillingState
  -- Specify the source table
FROM invoiceline
  -- Complete the join to the invoice table
LEFT JOIN invoice
ON invoiceline.InvoiceId = invoice.InvoiceId;

-- SELECT the fully qualified album_id column from the album table
SELECT 
  AlbumId,
  title,
  album.ArtistId,
  -- SELECT the fully qualified name column from the artist table
  name as artist
FROM album
-- Perform a join to return only rows that match from both tables
INNER JOIN artist ON album.ArtistId = artist.ArtistId
WHERE album.AlbumId IN (213,214)

SELECT 
  album.AlbumId,
  title,
  album.ArtistId,
  artist.name as artist
FROM album
INNER JOIN artist ON album.ArtistId = artist.ArtistId
-- Perform the correct join type to return matches or NULLS from the track table
RIGHT JOIN track on album.AlbumId = track.AlbumId
WHERE album.AlbumId IN (213,214)