#!/usr/bin/env bash
-- creates a table called first_table
-- within the current database in your MySQL server.

CREATE TABLE IF NOT EXISTS first_table
(
	id INT,
	name VARCHAR(256)
);
