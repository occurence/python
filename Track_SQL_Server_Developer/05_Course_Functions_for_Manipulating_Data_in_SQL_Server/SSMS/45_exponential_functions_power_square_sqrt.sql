-- Raise the number stored in the @number variable to the power from the @power variable.
-- Calculate the square of the @number variable (square means the power of 2).
-- Calculate the square root of the number stored in the @number variable.

DECLARE @number DECIMAL(4, 2) = 4.5;
DECLARE @power INT = 4;

SELECT
	@number AS number,
	@power AS power,
	-- Raise the @number to the @power
	POWER(@number, @power) AS number_to_power,
	-- Calculate the square of the @number
	SQUARE(@number) num_squared,
	-- Calculate the square root of the @number
	SQRT(@number) num_square_root;