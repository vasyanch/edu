CREATE PROCEDURE MailingListCount
AS
DECLARE @cnt INTEGER 
SELECT @cnt = COUNT(*)
FROM Customers
WHERE NOT cust_email IS NULL 
RETURN @cnt 