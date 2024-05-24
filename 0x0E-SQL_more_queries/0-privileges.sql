-- Script to list all privileges of MySQL users user_0d_1 and user_0d_2 on the server (localhost).
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
SELECT * FROM mysql.user WHERE User='user_0d_2';
