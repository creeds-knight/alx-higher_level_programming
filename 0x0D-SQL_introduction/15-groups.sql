--  A script to list the number of reccords with the same score in secon_table
SELECT 'score', COUNT(*) AS 'number'
FROM 'second_table'
GROUP BY 'score'
ORDER BY 'number' DESC;
