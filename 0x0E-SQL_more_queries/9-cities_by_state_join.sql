#!/usr/bin/env bash

SELECT c.id, c.name, s.name FROM cities AS c ON states AS s
WHERE s.id = c.state_id ORDER BY c.id
