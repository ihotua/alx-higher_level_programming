-- This script uses the hbtn_0d_tvshows database to list all genres
-- not linked to the show Dexter.
SELECT name
FROM tv_genres
WHERE name
NOT IN (SELECT y.name FROM tv_genres y
	RIGHT JOIN tv_show_genres m
	ON y.id = m.genre_id 
	RIGHT JOIN tv_shows p
	ON m.show_id = p.id 
	WHERE p.title = 'Dexter')
ORDER BY 1 ASC;
