-- List Number of Records with Same Score in second_table
-- from the hbtn_0c_0 database. Results display the score and the number of records
-- for each score, sorted by the number of records in descending order.

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
