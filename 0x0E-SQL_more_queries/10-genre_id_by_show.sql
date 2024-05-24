-- Script to list shows from hbtn_0d_tvshows with at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows 
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id 
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
