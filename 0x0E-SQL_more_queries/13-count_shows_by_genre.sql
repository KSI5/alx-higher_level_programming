-- List Genres and Number of Linked Shows
-- Execute: cat 14-genre_number_of_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

SELECT genre.`name` AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS genre
INNER JOIN tv_show_genres AS show_genre ON genre.`id` = show_genre.`genre_id`
GROUP BY genre.`name`
ORDER BY number_of_shows DESC;
