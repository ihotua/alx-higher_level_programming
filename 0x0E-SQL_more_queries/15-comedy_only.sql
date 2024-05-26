-- This is a that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT y.title
FROM tv_shows y
LEFT JOIN tv_show_genres m
ON y.id = m.show_id
LEFT JOIN tv_genres p
ON m.genre_id = p.id
WHERE p.name = 'Comedy'
ORDER BY 1 ASC;
