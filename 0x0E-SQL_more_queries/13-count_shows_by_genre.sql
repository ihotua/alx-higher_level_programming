-- This is a script that lists all genres from hbtn_0d_tvshows
-- and displays the number of shows linked to each.
SELECT m.name AS genre, count(y.show_id) AS number_of_shows
FROM tv_show_genres y 
LEFT JOIN tv_genres m 
ON y.genre_id = m.id
GROUP BY y.genre_id
ORDER BY 2 DESC;
