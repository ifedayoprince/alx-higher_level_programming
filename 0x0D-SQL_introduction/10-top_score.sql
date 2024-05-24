-- This script lists all records of the table second_table ordered by score descending.
USE $1;
SELECT score, name FROM second_table ORDER BY score DESC;
