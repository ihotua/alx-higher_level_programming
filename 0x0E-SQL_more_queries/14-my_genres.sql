-- This is a script that uses the hbtn_0d_tvshows database 
-- to list all genres of the show Dexter.
SELECT y.name
FROM tv_genres y
LEFT JOIN tv_show_genres m
ON y.id = m.genre_id
LEFT JOIN tv_shows p
ON m.show_id = p.id
WHERE p.title = 'Dexter'
ORDER BY 1 ASC;
