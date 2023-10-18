#!/usr/bin/env bash
-- Import in hbtn_0c_0 database this table dump: download
-- Write a script that displays the average temperature(Fahrenheit)
-- by city ordered by temperature (descending).

SELECT city, AVG(value) as avg_temp FROM temperatures
WHERE month IN(7, 8) GROUP BY city ORDER BY CITY DESC
LIMIT 3;
