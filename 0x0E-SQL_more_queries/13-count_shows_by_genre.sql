-- The script lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each displaying TV Show genre, Number of shows linked to this genre, does not display a genre that doesn’t have any shows linked, sorted in descending order by the number of shows linked.
SELECT tv_genres.genre AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;

