-- MySQL Database for testing

-- Creates a Test Database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create test user with password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Give privileges to the test user on the database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Give SELECT privilege
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
