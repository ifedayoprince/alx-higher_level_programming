-- This script counts the number of records with id = 89 in the table first_table.
USE $1;
SELECT COUNT(*) AS count FROM first_table WHERE id = 89;
