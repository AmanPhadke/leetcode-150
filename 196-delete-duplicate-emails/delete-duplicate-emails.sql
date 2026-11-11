-- WITH RankFilter AS(
--     SELECT email, 
--         ROW_NUMBER() OVER(PARTITION BY email ORDER BY id) as ranking
--     FROM Person
-- )

-- DELETE FROM RankFilter
-- WHERE ranking > 1

DELETE p1
FROM Person p1
JOIN Person p2
    ON p1.email = p2.email
    AND p2.id < p1.id
