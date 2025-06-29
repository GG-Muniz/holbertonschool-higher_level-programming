-- List all records wehre name is not empty
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;

