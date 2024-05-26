-- This is a script that lists all
-- cities contained in the database hbtn_0d_usa
SELECT m.id AS id, m.name AS name, y.name AS name 
FROM cities m 
INNER JOIN states y 
ON m.state_id = y.id
ORDER BY m.id ASC;
