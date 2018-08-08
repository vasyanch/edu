-- процедура для базы store
DROP PROCEDURE update_order_history;
DELIMITER //
CREATE PROCEDURE update_order_history(
    order_id INTEGER,
    status_id INTEGER,
    sum DECIMAL(18,2)
)
BEGIN 
    DECLARE now DATETIME;
    SET now = NOW();
    
    UPDATE sale_history
        SET active_to = now
	WHERE sale_history.sale_id = order_id AND 
          active_to IS NULL 
    LIMIT 1;
    
    INSERT INTO sale_history(sale_id, status_id, sale_sum, active_from, active_to)
         VALUES(order_id, status_id, sum, now, NULL);
END
//