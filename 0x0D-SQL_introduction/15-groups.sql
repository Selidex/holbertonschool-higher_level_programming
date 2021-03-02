-- counts people based on score values
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score DESC
