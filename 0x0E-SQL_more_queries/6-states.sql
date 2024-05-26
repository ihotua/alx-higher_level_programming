-- This script creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states
(
	PRIMARY KEY(id),
	id INT AUTO_INCREMENT NOT NULL UNIQUE,
	name VARCHAR(256)
);
