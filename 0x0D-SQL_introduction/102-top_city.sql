-- Displays the top 3 of cities temperature during July and August 
-- Ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp
    FROM temperatures
    WHERE month=7 || month=8
    GROUP BY city
    ORDER BY avg_temp DESC
    LIMIT 3;
