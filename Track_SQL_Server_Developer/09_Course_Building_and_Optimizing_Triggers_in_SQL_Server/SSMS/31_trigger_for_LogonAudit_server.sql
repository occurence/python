DROP TRIGGER IF EXISTS LogonAudit ON ALL SERVER;
GO
-- Create a trigger firing when users log on to the server
CREATE TRIGGER LogonAudit
-- Use ALL SERVER to create a server-level trigger
ON ALL SERVER WITH EXECUTE AS 'sa'
-- The trigger should fire after a logon
FOR LOGON
AS
	-- Save user details in the audit table
	INSERT INTO ServerLogonLog (LoginName, LoginDate, SessionID, SourceIPAddress)
	SELECT ORIGINAL_LOGIN(), GETDATE(), @@SPID, client_net_address
	FROM SYS.DM_EXEC_CONNECTIONS WHERE session_id = @@SPID;

/*
SELECT 
    name, 
    type_desc, 
    OBJECT_DEFINITION(object_id) AS definition
FROM sys.triggers
ORDER BY name;
*/