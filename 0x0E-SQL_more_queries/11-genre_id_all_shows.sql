-- Lists all shows contained in hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT OUTER JOIN tv_shows_genres
ON tv_shows.id = tv_show_genres.show_id IS NOT NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
