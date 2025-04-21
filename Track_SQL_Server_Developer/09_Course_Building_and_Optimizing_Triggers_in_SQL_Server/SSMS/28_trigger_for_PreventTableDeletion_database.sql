-- Add a trigger to disable the removal of tables
DROP TRIGGER IF EXISTS PreventTableDeletion ON DATABASE;
GO
CREATE TRIGGER PreventTableDeletion
ON DATABASE
FOR DROP_TABLE
AS
	RAISERROR ('You are not allowed to remove tables from this database.', 16, 1);
    -- Revert the statement that removes the table
    ROLLBACK;

/*
SELECT 
    name, 
    type_desc, 
    OBJECT_DEFINITION(object_id) AS definition
FROM sys.triggers
ORDER BY name;
*/