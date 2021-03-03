-- lists all cities from california
-- temporary comment due to requirements
SET @v1 := (SELECT id FROM states WHERE name = "California");
SELECT id, name FROM cities WHERE state_id = @v1;
