WITH LaggingLogs AS(
    SELECT *,
        LAG(temperature, 1) OVER (ORDER BY recordDate) as lagging,
        LAG(recordDate, 1) OVER (ORDER BY recordDate) as dateLag
    FROM Weather
)

SELECT id
FROM LaggingLogs
WHERE lagging < temperature
AND DATEDIFF(recordDate, dateLag) = 1
