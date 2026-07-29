-- MOVIE - TRACKER PROJECT .
-- Create database :- 
CREATE DATABASE movie_tracker;


-- Use our database as DEFAULT :-
USE movie_tracker;

-- Creating table in our database :-
CREATE TABLE movies(
id INT PRIMARY KEY AUTO_INCREMENT,
movie_name VARCHAR(100) NOT NULL,
genre VARCHAR(50) NOT NULL ,
language VARCHAR(50) NOT NULL ,
rating DECIMAL(3,1) NOT NULL ,
status VARCHAR(30) NOT NULL ,
release_year INT NOT NULL, 
AddOn_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

-- Inserting data to our databse :-
INSERT INTO movies(movie_name , genre , language , rating , status , release_year ) VALUES
('Dangal' , 'Inspiration' , 'Hindi' , 8.5 , 'Watched' , 2014),
('3 Idiots' , 'Entertainment' , 'Hindi' , 8.9 , 'Not Watched' , 2010),

-- Search data in our database :-
SELECT * FROM movies;