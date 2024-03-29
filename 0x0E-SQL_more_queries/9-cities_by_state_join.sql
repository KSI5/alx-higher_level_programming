-- List All Cities with States using JOIN
-- Execute: cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
