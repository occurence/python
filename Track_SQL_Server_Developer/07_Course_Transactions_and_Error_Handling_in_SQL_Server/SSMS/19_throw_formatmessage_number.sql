EXEC sp_addmessage @msgnum = 50002, @severity = 16, @msgtext = 'There are not enough %s bikes. You only have %d in stock.', @lang = N'us_english';

DECLARE @product_name AS NVARCHAR(50) = 'Trek CrossRip+ - 2018';
--Change the value
DECLARE @sold_bikes AS INT = 10;
DECLARE @current_stock INT;

SELECT @current_stock = stock FROM products WHERE product_name = @product_name;

DECLARE @my_message NVARCHAR(500) =
	FORMATMESSAGE(50002, @product_name, @current_stock);

IF (@current_stock - @sold_bikes < 0)
	THROW 50000, @my_message, 1;

-- Click Run Code (not Run Solution). You will see the error.
-- Set @sold_bikes to a value greater than @current_stock (e.g. 100).
EXEC sp_addmessage @msgnum = 50002, @severity = 16, @msgtext = 'There are not enough %s bikes. You only have %d in stock.', @lang = N'us_english';

DECLARE @product_name AS NVARCHAR(50) = 'Trek CrossRip+ - 2018';
--Change the value
DECLARE @sold_bikes AS INT = 100;
DECLARE @current_stock INT;

SELECT @current_stock = stock FROM products WHERE product_name = @product_name;

DECLARE @my_message NVARCHAR(500) =
	FORMATMESSAGE(50002, @product_name, @current_stock);

IF (@current_stock - @sold_bikes < 0)
	THROW 50000, @my_message, 1;