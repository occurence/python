BEGIN TRY
    INSERT INTO products(product_name, stock, price)
        VALUES('Trek Powerfly 5 - 2018', 10, 3499.99);
    SELECT 'Prooduct inserted correctly!' AS message;
END TRY
BEGIN CATCH
    SELECT 'An error occured! You are in the CATCH block' AS message;
END CATCH

BEGIN TRY
    INSERT INTO products(product_name, stock, price)
        VALUES('Super new Trek Powerfly', 5, 1499.99);
    SELECT 'Prooduct inserted correctly!' AS message;
END TRY
BEGIN CATCH
    SELECT 'An error occured! You are in the CATCH block' AS message;
END CATCH