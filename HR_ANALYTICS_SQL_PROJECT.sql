-- Query 1: Total Employees

SELECT COUNT(*) AS Total_Employees
FROM employees;
-- Query 2: Department-wise Employee Count
SELECT Department,
       COUNT(*) AS Employees
FROM employees
GROUP BY Department
ORDER BY Employees DESC;
-- Query 3: Attrition Summary

SELECT Attrition,
       COUNT(*) AS Employees
FROM employees
GROUP BY Attrition
ORDER BY Attrition;
-- Query 4: Department-wise Attrition Analysis

SELECT Department,
       COUNT(*) AS Employees,
       SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition,
       ROUND(
           SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
           2
       ) AS Attrition_Rate
FROM employees
GROUP BY Department
ORDER BY Attrition_Rate DESC;
-- Query 5: Attrition Reasons

SELECT Attrition_Reason,
       COUNT(*) AS Employees
FROM employees
WHERE Attrition = 'Yes'
GROUP BY Attrition_Reason
ORDER BY Employees DESC;
-- Query 6: Salary Analysis

SELECT 
    ROUND(AVG(Monthly_Salary), 2) AS Average_Monthly_Salary,
    MIN(Monthly_Salary) AS Minimum_Salary,
    MAX(Monthly_Salary) AS Maximum_Salary
FROM employees;
-- Query 7: Average Salary by Attrition

SELECT Attrition,
       ROUND(AVG(Monthly_Salary), 2) AS Average_Monthly_Salary
FROM employees
GROUP BY Attrition
ORDER BY Attrition;
-- Query 8: Overtime vs Attrition

SELECT Overtime,
       COUNT(*) AS Employees,
       SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition,
       ROUND(
           SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
           2
       ) AS Attrition_Rate
FROM employees
GROUP BY Overtime
ORDER BY Attrition_Rate DESC;
-- Query 9: Training Cost Analysis

SELECT
    ROUND(AVG(Training_Cost), 2) AS Average_Training_Cost,
    SUM(Training_Cost) AS Total_Training_Cost
FROM employees;
-- Query 10: Total Loss Analysis

SELECT
    SUM(Total_Loss) AS Total_Loss
FROM employees;
-- Query 11: High-Risk Employees

SELECT
    Employee_ID,
    Department,
    Job_Role,
    Job_Satisfaction,
    Overtime,
    Attrition
FROM employees
WHERE Job_Satisfaction <= 3
  AND Overtime = 'Yes'
  AND Attrition = 'Yes';
  -- Query 12: Department-wise Salary and Attrition

SELECT
    Department,
    ROUND(AVG(Monthly_Salary), 2) AS Average_Monthly_Salary,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Attrition_Rate
FROM employees
GROUP BY Department
ORDER BY Attrition_Rate DESC;
-- Query 13: High-Risk Departments

SELECT
    Department,
    COUNT(*) AS Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Attrition_Rate
FROM employees
GROUP BY Department
HAVING Attrition_Rate >= 50
ORDER BY Attrition_Rate DESC;