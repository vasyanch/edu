SELECT cust_name, cust_contact, cust_email
FROM Customers 
WHERE cust_name = 'Fun4All'
UNION 
SELECT cust_name, cust_contact, cust_email
FROM Customers 
WHERE cust_state IN ('IN', 'MI', 'IL')
ORDER BY cust_name, cust_contact 