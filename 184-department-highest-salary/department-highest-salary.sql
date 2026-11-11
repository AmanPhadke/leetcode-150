# Write your MySQL query statement below
WITH RankedRows AS(
SELECT  d.name AS Department, 
        e.name AS Employee, 
        e.salary AS Salary,
    RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) as ranking
FROM Employee e
JOIN Department d
    ON e.departmentId = d.id
)


SELECT Department, Employee, Salary
FROM RankedRows
WHERE ranking = 1