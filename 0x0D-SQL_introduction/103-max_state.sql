-- This script displays the max temperature of each state ordered by state name.
USE hbtn_0c_0;
SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
