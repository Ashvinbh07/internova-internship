-- Query 1 – Filtering and Sorting 
SELECT product_id, product_name, category, price 
FROM products WHERE category = 'Electronics' 
AND price > 1000 
ORDER BY price DESC; 

-- Query 2 – Aggregate Functions 
SELECT COUNT(*) AS total_products,
               SUM(price) AS total_price,
               ROUND(AVG(price), 2) AS average_price,
               MIN(price) AS minimum_price,
               MAX(price) AS maximum_price
FROM products;

