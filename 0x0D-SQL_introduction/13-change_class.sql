-- This script removes all records with a score <= 5 in the table second_table.
USE $1;
DELETE FROM second_table WHERE score <= 5;
