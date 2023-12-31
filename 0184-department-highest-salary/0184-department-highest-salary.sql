SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM Employee as e
JOIN Department as d ON e.departmentId = d.id
WHERE (e.salary, e.departmentId) IN (
    SELECT MAX(salary), departmentId
    FROM Employee
    GROUP BY departmentId
)

