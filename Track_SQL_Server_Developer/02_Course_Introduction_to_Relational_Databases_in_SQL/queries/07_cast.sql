-- Calculate the net amount as amount + fee
-- SELECT transaction_date, amount + CAST(fee AS INT) AS net_amount
SELECT transaction_date, amount + CONVERT (INT, CONVERT(VARCHAR(MAX),fee)) AS net_amount
FROM transactions;