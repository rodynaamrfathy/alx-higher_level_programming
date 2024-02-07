-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
-- lists all rows of a table linked to another table
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_shows.title, tv_genres.name
ORDER BY tv_shows.title, tv_genres.name;
