CREATE PROCEDURE NewOrder @cust_id CHAR(10)
AS
--jsldfja;sahghsdh
DECLARE @order_num INTEGER
SELECT @order_num = MAX(order_num)
FROM Orders
SELECT @order_num = @order_num + 1
INSERT INTO Orders(order_num, order_date, cust_id)
VALUES(@order_num, GETDATE(), @cust_id)
RETURN @order_num