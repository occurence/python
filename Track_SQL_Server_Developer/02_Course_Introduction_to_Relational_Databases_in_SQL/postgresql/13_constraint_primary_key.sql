-- Rename the organization column to id
ALTER TABLE organizations
RENAME COLUMN organization TO id;

SELECT column_name, data_type
FROM information_schema.columns 
WHERE table_name = 'organizations';

-- Make id a primary key
ALTER TABLE organizations
ADD CONSTRAINT organization_pk PRIMARY KEY (id);

-- Rename the university_shortname column to id
ALTER TABLE universities
RENAME COLUMN university_shortname TO id;

SELECT column_name, data_type
FROM information_schema.columns 
WHERE table_name = 'universities';

-- Make id a primary key
ALTER TABLE universities
ADD CONSTRAINT university_pk PRIMARY KEY (id);

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