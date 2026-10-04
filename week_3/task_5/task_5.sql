-- Problem 1 – Products Above Average Price 
SELECT *
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
)
ORDER BY price DESC;

-- Problem 2 – Highest-Priced Product 
SELECT *
FROM products
WHERE price = ( SELECT 
                    MAX(price)
                FROM products
              ); 

