-- a script that lists the number of records with the same score
-- in the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT `score`, COUNT(*) AS `record_count`
FROM second_table
GROUP `score`
ORDER BY `score` DESC;
