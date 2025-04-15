CREATE TABLE transactions (
 transaction_date date, 
 amount integer,
 fee text
);

SELECT * 
FROM transactions;

INSERT INTO transactions (transaction_date, amount, fee) 
VALUES ('1999-01-08', 500, '20')
,('2001-02-20', 403, '15')
,('2001-03-20', 3430, '35');

SELECT * 
FROM transactions;

-- Let's add a record to the table
INSERT INTO transactions (transaction_date, amount, fee) 
VALUES ('2018-09-24', 5454, '30');

SELECT * 
FROM transactions;