-- This is a script that lists all shows contained in
-- hbtn_0d_tvshows that have at least one genre linked.
SELECT m.title, y.genre_id
FROM tv_show_genres y
LEFT JOIN tv_shows m
ON y.show_id = m.id
ORDER BY m.title, y.genre_id ASC;
