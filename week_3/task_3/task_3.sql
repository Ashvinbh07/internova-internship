-- SQL Query: 
SELECT category,
               COUNT(*) AS total_products,
               ROUND(AVG(price), 2) AS average_price
FROM products
GROUP BY category
HAVING COUNT(*) > 2
ORDER BY average_price DESC;
