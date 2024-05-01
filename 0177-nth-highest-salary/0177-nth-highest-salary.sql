CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        SELECT DISTINCT Salary
        FROM (
            SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) AS Rank
            FROM Employee
        ) AS Ranked
        WHERE Rank = @N
    );
END