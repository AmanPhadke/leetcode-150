# Write your MySQL query statement below
WITH Immediates AS(
    SELECT customer_id,
        MIN(order_date) as immediate_date
    FROM Delivery
    GROUP BY customer_id
)


SELECT 
    ROUND(
        SUM(CASE 
                WHEN i.immediate_date = d.order_date
                 AND d.order_date = d.customer_pref_delivery_date
                THEN 1 
                ELSE 0 
            END) * 100.0 / COUNT(*), 2
    ) AS immediate_percentage
FROM Immediates i
JOIN Delivery d
    ON i.customer_id = d.customer_id
    AND i.immediate_date = d.order_date;

