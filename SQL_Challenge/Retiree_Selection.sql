-- drop tables if already exist
DROP TABLE IF EXISTS Employment_History;
DROP TABLE IF EXISTS Retirement_Titles;
DROP TABLE IF EXISTS Unique_Titles;
DROP TABLE IF EXISTS retiring_titles;
DROP TABLE IF EXISTS retiring_titles_by_dept;


-- perform query to join employees and titles data
SELECT Titles.emp_no, Titles.title, Titles.from_date, Titles.to_date, Employees.first_name, Employees.last_name, Employees.birth_date 
INTO Employment_History
FROM Titles
JOIN Employees ON Titles.emp_no=Employees.emp_no
ORDER BY Titles.from_date DESC;

-- perform query to filter birth_dates and sort for most recent titles
SELECT Employment_History.emp_no, title, dept_emp.dept_no, Employment_History.from_date, Employment_History.to_date, first_name, last_name, birth_date
INTO Retirement_Titles 
FROM Employment_History 
JOIN dept_emp ON dept_emp.emp_no=Employment_History.emp_no
WHERE birth_date 
BETWEEN '01/01/1952' AND '12/31/1955'
ORDER BY emp_no ASC;

-- Copy output query to csv
COPY Retirement_Titles TO 'C:\Users\Nodak\Documents\GitHub\SQL_Challenge\Output\Retirement_Titles.csv' DELIMITER ',' CSV HEADER;

-- perform query to ensure only most recent title is listed
SELECT DISTINCT ON(emp_no) emp_no, title, dept_name, from_date, to_date, first_name, last_name, birth_date
INTO Unique_Titles
FROM Retirement_Titles
JOIN departments ON Retirement_Titles.dept_no=departments.dept_no
WHERE to_date = '1/1/9999'
ORDER BY emp_no ASC;

-- Copy output query to csv
COPY Unique_Titles TO 'C:\Users\Nodak\Documents\GitHub\SQL_Challenge\Output\Unique_Titles.csv' DELIMITER ',' CSV HEADER;

-- perform query to count the number of employees from each title set to retire by department
SELECT COUNT(title), title, Unique_Titles.dept_name
INTO retiring_titles_by_dept
FROM Unique_Titles
GROUP BY title, Unique_Titles.dept_name
ORDER BY COUNT(title) DESC;

-- perform query to count number of employees for each title
SELECT COUNT(title), title 
INTO retiring_titles 
FROM Unique_Titles
GROUP BY title
ORDER BY COUNT(title) DESC;

-- Copy output query to csv
COPY retiring_titles TO 'C:\Users\Nodak\Documents\GitHub\SQL_Challenge\Output\retiring_titles.csv' DELIMITER ',' CSV HEADER;
COPY retiring_titles_by_dept TO 'C:\Users\Nodak\Documents\GitHub\SQL_Challenge\Output\retiring_titles_by_dept.csv' DELIMITER ',' CSV HEADER;
