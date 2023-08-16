-- List Dexter's Genres
-- Execute: cat 15-genre_dexter.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
-- This script lists all genres of the show Dexter from the database hbtn_0d_tvshows.

SELECT genre.`name`
FROM tv_shows AS tvshow
INNER JOIN tv_show_genres AS show_genre ON tvshow.`id` = show_genre.`show_id`
INNER JOIN tv_genres AS genre ON show_genre.`genre_id` = genre.`id`
WHERE tvshow.`title` = 'Dexter'
ORDER BY genre.`name` ASC;
