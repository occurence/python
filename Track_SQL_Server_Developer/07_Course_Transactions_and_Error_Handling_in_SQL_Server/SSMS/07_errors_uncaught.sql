BEGIN TRY
    SELECT non_existent_column FROM products;
END TRY
BEGIN CATCH
    SELECT 'CATCH BLOCK' AS message;
END CATCH