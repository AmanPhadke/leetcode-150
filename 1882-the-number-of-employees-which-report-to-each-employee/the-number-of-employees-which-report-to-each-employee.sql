# Write your MySQL query statement below
WITH managerInfo AS
(
    SELECT  reports_to as manager,
            COUNT(name) as reports_count, 
            ROUND(AVG(age)) as average_age

    FROM Employees
    WHERE reports_to IS NOT NULL
    GROUP BY manager
)

SELECT e.employee_id, e.name, m.reports_count, m.average_age
FROM managerInfo m
JOIN Employees e
    ON m.manager = e.employee_id
ORDER BY e.employee_id
