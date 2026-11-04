# Write your MySQL query statement below
-- WITH DupRows AS (
--     SELECT id, email,
--         ROW_NUMBER() OVER(PARTITION BY email ORDER BY id) as ranking
--     FROM Person
-- )

-- DELETE FROM DupRows
-- WHERE ranking > 1

DELETE p1
FROM Person p1
JOIN Person p2
WHERE p1.email = p2.email
AND p1.id > p2.id 
