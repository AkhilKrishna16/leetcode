# Write your MySQL query statement below
SELECT Email 
FROM Person
GROUP BY Email
HAVING COUNT(email) > 1;
