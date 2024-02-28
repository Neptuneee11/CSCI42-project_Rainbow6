CREATE DATABASE my_test_db;
CREATE USER 'test'@'localhost' IDENTIFIED BY 'Secret_1234';
GRANT ALL PRIVILEGES ON `my_test_db` . * TO 'test'@'localhost';
FLUSH PRIVILEGES; 