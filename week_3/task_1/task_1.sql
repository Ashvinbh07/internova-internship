-- Query 1 – Display all records
SELECT * FROM customers;

-- Query 2 – Select specific columns 
SELECT customer_name, city FROM customers;

-- Query 3 – Use column aliases 
SELECT customer_id AS "Customer ID",
               customer_name AS "Customer Name",
               city AS "Customer City"
FROM customers;
