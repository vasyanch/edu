SELECT vend_id, COUNT(*) AS num_prods 
FROM Products 
WHERE prod_price >= 1
GROUP BY vend_id
HAVING COUNT(*) >= 2
ORDER BY num_prods