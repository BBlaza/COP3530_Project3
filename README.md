# COP3530_Project3


##How to setup
1. Download the repository source code
2. Download the file title.basics.tsv.gz using this link: https://datasets.imdbws.com/ and put this file into the same repository as the main.py.
3. Download the file title.ratings.tsv.gz using the previous link.
4. Below are the instructions for having the current database on your own PostgreSQL.

##PostgreSQL Setup
1. Make sure you have PostgreSQL downloaded and installed.
2. Save this attached file "movie_db.dump" to any folder on your computer 
3. Make sure you save the bin folder path (inside your PostgreSQL folder) to system path environment variables
4. Create a database called movie_db in PostgreSQL.
5. Create a role called movie_user as well that can be able to connect to movie_db.
6. Then in your terminal run this command : PS C:\path\to\where\movie_db.dump\is> pg_restore -U movie_user -h your.server.ip -d movie_db movie_db.dump
7. You should have the database saved on your PostgreSQL now and you can view it in the pgAdmin4 app, which is in the PostgreSQL folder. 
