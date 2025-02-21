# Write your MySQL query statement below
SELECT *, 'Yes' as triangle
FROM Triangle
WHERE x + y > z AND x + z > y AND z + y > x
UNION 
SELECT *, 'No' as triangle
FROM Triangle 
WHERE x + y <= z OR z + x  <= y OR y + z <= x;