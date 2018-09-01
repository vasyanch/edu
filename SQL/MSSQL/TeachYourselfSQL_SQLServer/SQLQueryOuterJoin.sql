SELECT Customers.cust_id, COUNT(Orders.order_num) AS num_orders
FROM Customers LEFT OUTER JOIN Orders
ON Customers.cust_id = Orders.cust_id 
GROUP BY Customers.cust_id 