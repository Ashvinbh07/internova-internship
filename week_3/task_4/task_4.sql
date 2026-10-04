-- Query 1 - INNER JOIN
SELECT
    s.sale_id,
    c.customer_name,
    s.product_id,
    s.quantity,
    s.sale_date
FROM sales s
INNER JOIN customers c
    ON s.customer_id = c.customer_id;

-- Query 2 - LEFT JOIN
SELECT
    c.customer_id,
    c.customer_name,
    c.city,
    s.sale_id,
    s.quantity
FROM customers c
LEFT JOIN sales s
    ON c.customer_id = s.customer_id
ORDER BY c.customer_id;

-- Query 3 - RIGHT JOIN
SELECT
    c.customer_id,
    c.customer_name,
    s.sale_id,
    s.product_id,
    s.quantity
FROM customers c
RIGHT JOIN sales s
    ON c.customer_id = s.customer_id
ORDER BY s.sale_id;
