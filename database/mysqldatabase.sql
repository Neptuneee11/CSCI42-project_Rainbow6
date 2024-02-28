CREATE DATABASE my_test_db;
CREATE USER 'test'@'localhost' IDENTIFIED BY 'Secret_1234';
GRANT ALL PRIVILEGES ON `my_test_db` . * TO 'test'@'localhost';
FLUSH PRIVILEGES; 
USE my_test_db;


CREATE TABLE Customer (
	customer_id INT NOT NULL UNIQUE PRIMARY KEY,
    first_name VARCHAR(15),
    last_name VARCHAR(15)
);

