-- a statements without join
SELECT id, name
  FROM cities
  WHERE state_id IN
  (SELECT id
	   FROM states
	   WHERE name = "California")
  ORDER BY id;
