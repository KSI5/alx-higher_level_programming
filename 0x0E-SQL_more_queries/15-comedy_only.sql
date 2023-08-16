-- List Comedy Shows
-- Execute: cat 17-comedy_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
-- This script lists all Comedy shows from the database hbtn_0d_tvshows.

SELECT tvshow.`title`
FROM tv_shows AS tvshow
JOIN tv_show_genres AS show_genre ON tvshow.`id` = show_genre.`show_id`
JOIN tv_genres AS genre ON show_genre.`genre_id` = genre.`id`
WHERE genre.`name` = 'Comedy'
ORDER BY tvshow.`title` ASC;
