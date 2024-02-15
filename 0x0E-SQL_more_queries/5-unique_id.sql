-- A script to create a table unique_id  on MYSQL server
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT UNIQUE,
	name VARCHAR(256)
);
