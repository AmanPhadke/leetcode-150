# Write your MySQL query statement below
WITH TopSalaries AS(
SELECT d.name AS Department, 
    e.name AS Employee, 
    e.salary AS Salary,
    DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) rankings
FROM Employee e
JOIN Department d
    ON d.id = e.departmentId
)

SELECT Department, Employee, Salary
FROM TopSalaries
WHERE rankings <= 3
