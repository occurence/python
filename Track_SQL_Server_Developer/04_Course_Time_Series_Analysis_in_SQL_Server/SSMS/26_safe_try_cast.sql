DECLARE
	@GoodDateINTL NVARCHAR(30) = '2019-03-01 18:23:27.920',
	@GoodDateDE NVARCHAR(30) = '13.4.2019',
	@GoodDateUS NVARCHAR(30) = '4/13/2019',
	@BadDate NVARCHAR(30) = N'SOME BAD DATE';

-- -- The prior solution using TRY_CONVERT
-- SELECT
-- 	TRY_CONVERT(DATETIME2(3), @GoodDateINTL) AS GoodDateINTL,
-- 	TRY_CONVERT(DATE, @GoodDateDE) AS GoodDateDE,
-- 	TRY_CONVERT(DATE, @GoodDateUS) AS GoodDateUS,
-- 	TRY_CONVERT(DATETIME2(3), @BadDate) AS BadDate;

SELECT
	-- Fill in the correct data type based on our input
	TRY_CAST(@GoodDateINTL AS DATETIME2(3)) AS GoodDateINTL,
    -- Be sure to match these data types with the
    -- TRY_CONVERT() examples above!
	TRY_CAST(@GoodDateDE AS DATE) AS GoodDateDE,
	TRY_CAST(@GoodDateUS AS DATE) AS GoodDateUS,
	TRY_CAST(@BadDate AS DATETIME2(3)) AS BadDate;