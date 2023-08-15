-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
-- Display the max temperature of each state (ordered by State name)
SELECT state, MAX(temperature) AS max_temperature FROM temperatures GROUP BY state ORDER BY state;
