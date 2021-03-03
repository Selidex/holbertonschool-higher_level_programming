-- lists all genres
-- and tells how many whos have that genre
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres
LEFT JOIN tv_genres
ON tv_genres.id = genre_id
GROUP BY genre_id
ORDER BY number_of_shows DESC;
