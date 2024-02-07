-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- lists all rows of a database meeting a condition
SELECT tv_genres.name AS 'name'
COUNT (tv_show_genres.genre_id AS 'no')
FROM tv_genres
RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY no DESC;
