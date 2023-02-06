-- Perform check if tables exist
DROP TABLE IF EXISTS Mentor_List;
DROP TABLE IF EXISTS Mentor_Summary;

-- create mentor list of eligible employees
SELECT DISTINCT ON(dept_emp.emp_no) dept_emp.emp_no, employees.first_name, employees.last_name, employees.birth_date, dept_emp.from_date, dept_emp.to_date, titles.title, titles.from_date AS title_date, departments.dept_name
INTO Mentor_List
FROM dept_emp
JOIN employees ON dept_emp.emp_no=employees.emp_no
JOIN titles ON dept_emp.emp_no=titles.emp_no
JOIN departments ON dept_emp.dept_no=departments.dept_no
WHERE dept_emp.to_date='1/1/9999' AND employees.birth_date BETWEEN '1/1/1965' AND '12/31/1965'
ORDER BY dept_emp.emp_no ASC, titles.from_date DESC;

-- output csv
COPY Mentor_List TO 'C:\Users\Nodak\Documents\GitHub\SQL_Challenge\Output\Mentor_List.csv' DELIMITER ',' CSV HEADER;

-- create table to show breakdown of mentors by position and department
SELECT COUNT(Mentor_List.title), Mentor_List.title, Mentor_List.dept_name
INTO Mentor_Summary
FROM Mentor_List
GROUP BY Mentor_List.title, Mentor_List.dept_name;

-- output csv
COPY Mentor_Summary TO 'C:\Users\Nodak\Documents\GitHub\SQL_Challenge\Output\Mentor_Summary.csv' DELIMITER ',' CSV HEADER;
