#!/usr/bin/env bash
-- Write a script that creates the table id_not_null on your MySQL server.

CREATE TABLE IF NOT EXISTS unique_id
(
        id INT DEFAULT 1,
	name VARCHAR(256)
);
