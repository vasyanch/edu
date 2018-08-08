SELECT C.*, O.order_num, O.order_date, OI.prod_id, OI.quantity, OI.item_price, OI.quantity * OI.item_price AS total_price 
FROM Customers AS C, Orders AS O, OrderItems AS OI
WHERE C.cust_id = O.cust_id 
AND O.order_num = OI.order_num 
AND prod_id = 'RGAN01'