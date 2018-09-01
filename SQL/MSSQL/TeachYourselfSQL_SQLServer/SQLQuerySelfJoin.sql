SELECT cl.cust_id, cl.cust_name, cl.cust_contact 
FROM Customers AS cl, Customers AS c2
WHERE cl.cust_name = c2.cust_name
AND c2.cust_contact = 'Jim Jones'