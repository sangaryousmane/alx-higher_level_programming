#!/usr/bin/env bash
-- Write a script that lists all the cities
-- of California that can be found in the database hbtn_0d_usa.

SELECT *FROM cities AS c, states AS s WHERE c.id = s.id AND s.name = "California"
ORDER BY c.id ASC;
