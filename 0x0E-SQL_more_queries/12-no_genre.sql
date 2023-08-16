-- This script lists all shows without linked genres from the database hbtn_0d_tvshows
-- Execute: cat 12-shows_without_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows


SELECT CONCAT(tv_shows.title, ' - ', 'NULL') AS show_info
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title ASC;
