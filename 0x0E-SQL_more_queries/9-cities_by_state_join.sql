-- lists all cities within the database
-- format city id, city name, state name
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
