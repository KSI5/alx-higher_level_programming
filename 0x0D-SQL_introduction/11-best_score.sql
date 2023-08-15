-- List the score greather than or equal to 10
-- from the second_table in the hbtn_0c_0 database.
-- Results display both the score and the name, ordered by score (top first).


SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
