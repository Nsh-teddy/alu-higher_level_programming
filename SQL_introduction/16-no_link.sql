-- Lists all records with non-null and non-empty names from second_table, showing score and name ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
