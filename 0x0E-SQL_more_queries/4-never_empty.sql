-- Create Table id_not_null
-- Execute: cat 4-id_not_null.sql | mysql -hlocalhost -uroot -p hbtn_0d_2

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
