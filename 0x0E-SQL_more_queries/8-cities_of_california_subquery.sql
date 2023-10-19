#!/usr/bin/env bash
-- Write a script that lists all the cities
-- of California that can be found in the database hbtn_0d_usa.

SELECT *FROM states WHERE states.id = cities.state_id ORDER BY id ASC;
