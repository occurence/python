-- Find out the sign of the result (positive or negative).

DECLARE @number1 DECIMAL(18,2) = -5.4;
DECLARE @number2 DECIMAL(18,2) = 7.89;
DECLARE @number3 DECIMAL(18,2) = 13.2;
DECLARE @number4 DECIMAL(18,2) = 0.003;

DECLARE @result DECIMAL(18,2) = @number1 * @number2 - @number3 - @number4;
SELECT 
	@result AS result,
	-- Show the absolute value of the result
	ABS(@result) AS abs_result,
	-- Find the sign of the result
	SIGN(@result) AS sign_result;