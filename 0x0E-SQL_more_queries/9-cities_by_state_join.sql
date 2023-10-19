#!/usr/bin/env bash

SELECT c.id, c.name, s.name FROM cities AS s ON cities AS c
WHERE s.id = c.state_id ORDER BY c.id
