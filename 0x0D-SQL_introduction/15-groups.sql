-- counts people based on score values
SELECT score, COUNT(*)
FROM second_table
GROUP BY score DESC
