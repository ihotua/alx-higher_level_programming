-- This is a script that lists all shows contained in
-- hbtn_0d_tvshows without a genre linked
SELECT m.title, y.genre_id
FROM tv_show_genres y
RIGHT JOIN tv_shows m
ON y.show_id = m.id
WHERE y.show_id IS NULL
ORDER BY m.title, y.genre_id ASC;
