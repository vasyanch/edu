CREATE VIEW OrderItemsExpanded AS 
SELECT order_num, prod_id, Quantity, item_price, quantity * item_price AS expanded_price
FROM OrderItems

CREATE VIEW CustomerEmailList
AS SELECT cust_id, cust_name, cust_email
FROM Customers
WHERE cust_email IS NOT NULL 

CREATE VIEW VendorsLocation
AS SELECT RTRIM(vend_name) + '(' + RTRIM(vend_country) +')' AS vend_title
FROM Vendors

CREATE VIEW ProductCustomers
AS SELECT cust_name, cust_contact, prod_id
FROM Customers, Orders, OrderItems
WHERE Customers.cust_id = Orders.cust_id
AND Orders.order_num = OrderItems.order_num 
