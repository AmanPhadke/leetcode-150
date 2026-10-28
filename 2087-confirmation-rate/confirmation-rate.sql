# Write your MySQL query statement below
SELECT s.user_id, IFNULL(
    ROUND(
            (
        SELECT COUNT(action)
        FROM Confirmations
        WHERE action = 'confirmed' AND s.user_id = user_id
    ) / COUNT(c.action), 
    2),
    0) as confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
    ON s.user_id = c.user_id
GROUP BY s.user_id