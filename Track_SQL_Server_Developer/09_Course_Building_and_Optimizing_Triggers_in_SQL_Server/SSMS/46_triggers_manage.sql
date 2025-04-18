-- Get the disabled triggers
SELECT name,
	   object_id,
	   parent_class_desc
FROM sys.triggers
WHERE is_disabled = 1;

-- Check for unchanged server triggers
SELECT *
FROM sys.server_triggers
WHERE create_date = modify_date;

-- Get the database triggers
SELECT *
FROM sys.triggers
WHERE parent_class_desc = 'DATABASE';