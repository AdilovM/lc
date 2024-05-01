CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        SELECT Salary
        FROM (
            SELECT Salary, ROW_NUMBER() OVER (ORDER BY Salary DESC) AS RowNum
            FROM (
                SELECT DISTINCT Salary
                FROM Employee
            ) AS DistinctSalaries
        ) AS Ranked
        WHERE RowNum = @N
    );
END