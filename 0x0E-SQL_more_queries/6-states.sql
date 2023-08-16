-- Create Database hbtn_0d_usa and Table states
-- Execute: cat 5-force_usa.sql | mysql -hlocalhost -uroot -p

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(256) NOT NULL
);
