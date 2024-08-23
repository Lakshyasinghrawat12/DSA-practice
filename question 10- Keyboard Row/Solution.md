# Row Definitions:

**row1**, **row2**, and **row3** are sets containing the characters of each row on the keyboard. Using sets makes it easy to check if all characters of a word are contained within a particular row.

# Case Insensitivity:

- The words are converted to lowercase using word.lower() to ensure the comparison is case-insensitive.
Subset Check:

- **lowercase_word.issubset(row1)** checks if all characters of word are in row1. The same check is done for row2 and row3.


# Adding to Result:

- If any of the checks pass, the word is added to the result list.