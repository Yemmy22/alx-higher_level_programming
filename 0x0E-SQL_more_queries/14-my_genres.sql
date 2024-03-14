-- This script lists all Comedy shows in the database hbtn_0d_tvshows. The tv_genres table contains only one record where name = Comedy (but the id is different). Each record displays tv_shows.title and the table is sorted in ascending order by the show title.
SELECT tv_genres.name
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
