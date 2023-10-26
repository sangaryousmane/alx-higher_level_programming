#!/usr/bin/env bash
-- Write a script that lists all the cities
-- of California that can be found in the database hbtn_0d_usa.

SELECT *FROM cities AS c WHERE c.id = c.state_id ORDER BY id ASC;
