-- List Privileges of MySQL Users
-- Execute: cat 0-show_grants.sql | mysql -hlocalhost -uroot -p
-- This script lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (localhost).

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
