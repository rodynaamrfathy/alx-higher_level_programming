-- a script that creates the database hbtn_0d_usa
-- and the table states (in the database hbtn_0d_usa)
CREATE DATABASE hbtn_0d_usa;
-- CREATE TABLE
USE hbtn_0d_usa
CREATE TABLE states(
	id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
