DELETE 
FROM billing
WHERE payer_email IS NULL OR payer_email = '' OR recipient_email = '' OR recipient_email IS NULL;

SELECT * 
FROM billing
