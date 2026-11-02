# Write your MySQL query statement below
WITH Singles AS (
    SELECT employee_id, COUNT(DISTINCT department_id) AS dep_count
    FROM Employee
    GROUP BY employee_id
)

SELECT e.employee_id, e.department_id
FROM Singles s
JOIN Employee e
    ON s.employee_id = e.employee_id
WHERE e.primary_flag = 'Y' OR s.dep_count = 1

