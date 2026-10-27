# Write your MySQL query statement below
WITH Prev_Temperature AS(
    SELECT id,
    temperature,
    recordDate,
        LAG(temperature, 1) OVER (ORDER BY recordDate) AS prev_temp,
        LAG(recordDate, 1) OVER (ORDER BY recordDate) AS prev_date
    FROM Weather
)
SELECT id
FROM Prev_Temperature
WHERE prev_temp < temperature AND DATEDIFF(recordDate, prev_date) = 1