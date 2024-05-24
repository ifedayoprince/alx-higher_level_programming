-- This script updates the score of Bob to 10 in the table second_table.
USE $1;
UPDATE second_table SET score = 10 WHERE name = 'Bob';
