-- Select 5 characters from the email address, starting with position 3.
SELECT 
	email,
    -- Extract 5 characters from email, starting at position 3
	SUBSTRING(email, 3, 5) AS some_letters
FROM voters;

-- Extract the fruit names from the following sentence: "Apples are neither oranges nor potatoes".
DECLARE @sentence NVARCHAR(200) = 'Apples are neither oranges nor potatoes.'
SELECT
	-- Extract the word "Apples" 
	SUBSTRING(@sentence, 1, 6) AS fruit1,
    -- Extract the word "oranges"
	SUBSTRING(@sentence, 20, 7) AS fruit2;