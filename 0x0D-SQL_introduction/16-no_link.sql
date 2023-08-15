-- This script lists records with a name value from the second_table
-- in the hbtn_0c_0 database. Results display the score and the name for each record,
-- ordered by score in descending order.

SELECT score, name FROM second_table WHERE name!='' OR name IS NOT NULL ORDER BY score DESC;
