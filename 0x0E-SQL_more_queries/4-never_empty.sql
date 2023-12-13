-- a script that creates the table id_not_null on  MySQL server.
-- id INT with the default value 1
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256)
);
