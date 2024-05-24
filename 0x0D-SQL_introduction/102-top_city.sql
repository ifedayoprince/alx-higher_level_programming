-- This script displays the top 3 cities by temperature during July and August.
USE hbtn_0c_0;
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
