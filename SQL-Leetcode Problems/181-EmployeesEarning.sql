SELECT E.name AS Employee
FROM EMPLOYEE E
JOIN EMPLOYEE M
ON E.managerId = M.id
WHERE E.salary > M.salary
