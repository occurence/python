-- Add the new column to the table
ALTER TABLE professors 
ADD COLUMN id serial;

-- Make id a primary key
ALTER TABLE professors 
ADD CONSTRAINT professors_pkey PRIMARY KEY (id);

-- Have a look at the first 10 rows of professors
SELECT *
FROM professors
LIMIT 10;

SELECT 
    tc.table_name,
    tc.constraint_name,
    tc.constraint_type,
    kcu.column_name
FROM information_schema.table_constraints AS tc
LEFT JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
    AND tc.table_name = kcu.table_name
WHERE tc.table_name IN ('professors', 'universities', 'organizations', 'affiliations');