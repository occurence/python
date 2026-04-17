BEGIN TRY
    INSERT INTO products(product_name, stock, price)
        VALUES('Trek Powerfly 5 - 2018', 10, 3499.99);
    SELECT 'Prooduct inserted correctly!' AS message;
END TRY
BEGIN CATCH
    BEGIN TRY
        INSERT INTO errors
            VALUES('Error from nested function');
        SELECT 'Error from nested function' AS message;
    END TRY
    BEGIN CATCH
        SELECT 'OUTER CATCH BLOCK' AS 'Error_from',
        ERROR_NUMBER() AS Error_number,
        ERROR_MESSAGE() AS Error_message;
    END CATCH
    -- SELECT ERROR_NUMBER() AS Error_number,
    --        ERROR_SEVERITY() AS Error_severity,
    --        ERROR_STATE() AS Error_state,
    --        ERROR_PROCEDURE() AS Error_procedure,
    --        ERROR_LINE() AS Error_line,
    --        ERROR_MESSAGE() AS Error_message;
END CATCH