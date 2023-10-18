#!/usr/bin/env bash
-- Import in hbtn_0c_0 database this table dump: download
-- Write a script that displays the average temperature(Fahrenheit)
-- by city ordered by temperature (descending).

SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state ORDER BY max_temp DESC;
