#!/usr/bin/env bash
-- Import the database dump from hbtn_0d_tvshows to your MySQL server:
-- download (same as 16-shows_by_genre.sql)
-- Write a script that uses the hbtn_0d_tvshows
-- database to list all genres not linked to the show Dexter

SELECT name FROM tv_genres WHERE name NOT IN (
SELECT tg.name FROM tv_show_genres AS tsg
    JOIN tv_genres AS tg ON tsg.genre_id = tg.id
    JOIN tv_shows AS ts ON tsg.show_id = ts.id WHERE ts.title = 'Dexter'
);
