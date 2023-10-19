Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
1. Root user
Write a script that creates the MySQL server user user_0d_1.

user_0d_1 should have all privileges on your MySQL server
The user_0d_1 password should be set to user_0d_1_pwd
If the user user_0d_1 already exists, your script should not fail
.
.
.
16. List shows and genres
Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 15-comedy_only.sql)

Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

If a show doesn’t have a genre, display NULL in the genre column
Each record should display: tv_shows.title - tv_genres.name
Results must be sorted in ascending order by the show title and genre name
You can use only one SELECT statement
The database name will be passed as an argument of the mysql command
17. Not my genre
Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 16-shows_by_genre.sql)

Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
.
.
.
20. Best genre
Import the database dump from hbtn_0d_tvshows_rate to your MySQL server: download (same as 102-rating_shows.sql)

Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
