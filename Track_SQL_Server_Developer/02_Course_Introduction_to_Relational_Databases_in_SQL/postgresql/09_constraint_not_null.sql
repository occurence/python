SELECT column_name, data_type, is_nullable
FROM information_schema.columns 
WHERE table_name = 'professors';

-- Disallow NULL values in firstname
ALTER TABLE professors 
ALTER COLUMN firstname SET NOT NULL;

SELECT column_name, data_type, is_nullable
FROM information_schema.columns 
WHERE table_name = 'professors';

-- Disallow NULL values in lastname
ALTER TABLE professors
ALTER COLUMN lastname SET NOT NULL