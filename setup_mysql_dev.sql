-- MySQL Database

-- Creates a Database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user with password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Give privileges to the user on the database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Give SELECT privilege
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
