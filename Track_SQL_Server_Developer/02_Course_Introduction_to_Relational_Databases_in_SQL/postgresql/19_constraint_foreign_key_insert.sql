-- Try to insert a new professor
INSERT INTO professors (firstname, lastname, university_id)
-- VALUES ('Albert', 'Einstein', 'MIT');
VALUES ('Albert', 'Einstein', 'UZH');

-- Have a look at the table
SELECT * FROM professors WHERE firstname='Albert' AND lastname='Einstein';