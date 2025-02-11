/*
-- Enable OPENROWSET if not enabled
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'Ad Hoc Distributed Queries', 1;
RECONFIGURE;

EXEC sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'AllowInProcess', 1;
EXEC sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'DynamicParameters', 1;

-- Import CSV with OPENROWSET
SELECT * INTO dbo.MyTable
FROM OPENROWSET(
    'Microsoft.ACE.OLEDB.12.0',
    'Text;Database=D:\STUDY\python\Track_SQL_Server_Developer\01_Course_Introduction_to_SQL_Server\datasets\college.csv;',
    'SELECT * FROM [File.csv]'
);
*/

DROP TABLE IF EXISTS college;
-- Create a table for the university_professors entity type
CREATE TABLE college(
  firstname text,
  lastname text,
  university text,
  university_shortname text,
  university_city text,
  [function] text,
  organization text,
  organization_sector text
);

BULK INSERT college
FROM 'D:\STUDY\python\Track_SQL_Server_Developer\01_Course_Introduction_to_SQL_Server\datasets\college.csv'
WITH (
    FORMAT = 'CSV',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    CODEPAGE = '65001'
);

-- Doublecheck the contents of college
SELECT * 
FROM college;