SELECT p.product_name, c.category_name, p.price
FROM product as p INNER JOIN category as c ON p.category_id = c.category_id
ORDER BY p.category_id 


