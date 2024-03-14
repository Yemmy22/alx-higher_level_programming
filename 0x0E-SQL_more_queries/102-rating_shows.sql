-- This script that lists all genres in the database hbtn_0d_tvshows_rate by their rating. Each record displays tv_genres.name - rating sum. The result is sorted in descending order by their rating
SELECT tv_shows.title, COALESCE(SUM(tv_show_ratings.rate), 0) AS rating_sum
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;

