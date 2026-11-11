-- WITH RowRanks AS(
--     SELECT salary,
--         DENSE_RANK() OVER(ORDER BY salary) as ranks
--     FROM Employee
-- )

-- SELECT (CASE WHEN ranks = 2 THEN salary ELSE NULL END) AS SecondHighestSalary
-- FROM RowRanks 
-- ORDER BY SecondHighestSalary DESC
-- LIMIT 1

SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) as SecondHighestSalary
