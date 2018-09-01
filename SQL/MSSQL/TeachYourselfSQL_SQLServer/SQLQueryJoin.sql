SELECT cust_name, cust_contact
FROM Customers, OrderItems, Orders 
WHERE OrderItems.order_num = Orders.order_num
AND Customers.cust_id = Orders.cust_id
AND prod_id = 'RGAN01'