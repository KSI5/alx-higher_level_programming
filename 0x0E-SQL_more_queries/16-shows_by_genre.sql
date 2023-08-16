-- List Shows with Genres
-- Execute: cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

SELECT tvshow.`title`, IFNULL(GROUP_CONCAT(genre.`name` ORDER BY genre.`name` ASC SEPARATOR ', '), 'NULL') AS genre
FROM tv_shows AS tvshow
LEFT JOIN tv_show_genres AS show_genre ON tvshow.`id` = show_genre.`show_id`
LEFT JOIN tv_genres AS genre ON show_genre.`genre_id` = genre.`id`
GROUP BY tvshow.`title`
ORDER BY tvshow.`title` ASC, genre ASC;
