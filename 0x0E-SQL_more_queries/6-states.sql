-- creates a database and a table
-- name cant be null, id auto generated, unique
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(256) NOT NULL,
UNIQUE(id),
PRIMARY KEY(id))
