-- Create Database hbtn_0d_2 and User user_0d_2
-- Execute: cat 2-create_user_and_database.sql | mysql -hlocalhost -uroot -p

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
