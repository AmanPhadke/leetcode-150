WITH Leads AS(
SELECT num,
    LEAD(num, 1) OVER (ORDER BY id) as lead1,
    LEAD(num, 2) OVER (ORDER BY id) as lead2
FROM Logs
)

SELECT DISTINCT num AS ConsecutiveNums
FROM Leads
WHERE num = lead1 AND num = lead2
