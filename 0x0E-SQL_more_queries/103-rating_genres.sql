-- This script lists all genres in the database hbtn_0d_tvshows_rate by their rating. Each record displays tv_genres.name - rating sum. It is sorted in descending order by their rating.
SELECT tv_genres.name, COALESCE(SUM(tv_show_ratings.rate), 0) AS rating_sum
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
