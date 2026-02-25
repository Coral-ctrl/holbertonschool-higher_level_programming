-- creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the database
USE hbtn_0d_usa;

CREATE TABLE IT NOT EXISTS states (
       id INT NOT NULL AUTO_INCREMENT,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY (id)
);
