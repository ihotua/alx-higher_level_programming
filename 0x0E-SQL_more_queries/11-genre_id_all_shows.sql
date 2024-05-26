-- This is a script that lists all shows contained in the database.
SELECT m.title, y.genre_id
FROM tv_show_genres y
RIGHT JOIN tv_shows m
ON y.show_id = m.id
ORDER BY m.title, y.genre_id ASC;
