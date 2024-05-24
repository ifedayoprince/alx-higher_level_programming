-- This script lists all records of the table second_table excluding rows without a name value.
USE $1;
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
