-- Create a view with the top artists in 2017
DROP VIEW IF EXISTS long_reviews;
GO
CREATE VIEW long_reviews AS
SELECT content.reviewid,
    content.content
   FROM content
  --WHERE (len(content.content) > 4000);
  WHERE DATALENGTH(content.content) > 4000;
GO

-- Revoke everyone's update and insert privileges
REVOKE UPDATE, INSERT ON long_reviews FROM public; 
GO

-- Grant the editor update and insert privileges 
GRANT UPDATE, INSERT ON long_reviews TO public;
GO

SELECT * FROM information_schema.views
WHERE table_schema not in ('pg_catalog', 'information_schema');

SELECT 
    dp.state_desc AS PermissionState,
    dp.permission_name AS PermissionType,
    pr.name AS Grantee,
    ob.name AS ObjectName,
    ob.type_desc AS ObjectType
FROM 
    sys.database_permissions dp
JOIN 
    sys.objects ob ON dp.major_id = ob.object_id
JOIN 
    sys.database_principals pr ON dp.grantee_principal_id = pr.principal_id
WHERE 
    ob.name = 'long_reviews';
