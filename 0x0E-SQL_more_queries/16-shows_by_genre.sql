-- This is a script that lists all shows, and all genres linked 
-- to that show, from the database hbtn_0d_tvshows.
SELECT y.title, p.name
FROM tv_shows y
LEFT JOIN tv_show_genres m
ON y.id = m.show_id
LEFT JOIN tv_genres p
ON m.genre_id = p.id
ORDER BY 1,2 ASC;
