# How does pandas handle self joins?
# Select the false statement about merging a table to itself.

# Possible Answers
# Select one answer

# You can merge a table to itself with a right join.
# Merging a table to itself can allow you to compare values in a column to other values in the same column.
# The pandas module limits you to one merge where you merge a table to itself. You cannot repeat this process over and over. # False and Correct answer
# Merging a table to itself is like working with two separate tables.

# Perfect! This statement is false. 
# pandas treats a merge of a table to itself the same as any other merge. 
# Therefore, it does not limit you from chaining multiple .merge() methods together.