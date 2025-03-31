-- Create the function
CREATE FUNCTION dbo.ConvertDollar
	-- Specify @DollarAmt parameter
	(@DollarAmt numeric(18,2),
     -- Specify ExchangeRate parameter
     @ExchangeRate numeric(18,2))
-- Specify return data type
RETURNS numeric(18,2)
AS
BEGIN
RETURN
	-- Multiply @ExchangeRate and @DollarAmt
	(SELECT @ExchangeRate * @DollarAmt)
END;

/*
SELECT 
    name, 
    type_desc, 
    OBJECT_DEFINITION(object_id) AS definition
FROM sys.objects
WHERE type IN ('FN', 'IF', 'TF')
ORDER BY name;
*/