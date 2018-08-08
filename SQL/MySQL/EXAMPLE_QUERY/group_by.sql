/* база project_simple 
SELECT client_name, 
       AVG(DATEDIFF(project_finish, project_start)) as avg_days, 
       MAX(DATEDIFF(project_finish, project_start)) as max_days, 
       MIN(DATEDIFF(project_finish, project_start)) as min_days
FROM Project
WHERE project_finish IS NOT NULL
GROUP BY client_name
ORDER BY max_days  DESC
LIMIT 10;