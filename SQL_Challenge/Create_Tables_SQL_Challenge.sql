-- Create new tables, copy csv files into tables.
DROP TABLE IF EXISTS Employees CASCADE;
DROP TABLE IF EXISTS Salaries CASCADE;
DROP TABLE IF EXISTS Titles CASCADE;
DROP TABLE IF EXISTS Dept_Emp CASCADE;
DROP TABLE IF EXISTS Dept_Manager CASCADE;
DROP TABLE IF EXISTS Departments CASCADE;

CREATE TABLE IF NOT EXISTS Employees (
	emp_no INT,
	birth_date DATE,
	first_name TEXT,
	last_name TEXT,
	gender TEXT,
	hire_date DATE,
	PRIMARY KEY (emp_no)
);

CREATE TABLE IF NOT EXISTS Titles (
	emp_no INT,
	title TEXT,
	from_date DATE,
	to_date DATE,
	FOREIGN KEY (emp_no) REFERENCES Employees(emp_no)
);

CREATE TABLE IF NOT EXISTS Salaries (
	emp_no INT,
	salary DECIMAL,
	from_date DATE,
	to_date DATE,
	PRIMARY KEY (emp_no),
	FOREIGN KEY (emp_no) REFERENCES Employees(emp_no)
);

CREATE TABLE IF NOT EXISTS Dept_Manager (
	dept_no TEXT,
	emp_no INT,
	from_date DATE,
	to_date DATE,
	PRIMARY KEY (emp_no),
	FOREIGN KEY (emp_no) REFERENCES Employees(emp_no)
);

CREATE TABLE IF NOT EXISTS Dept_Emp (
	emp_no INT,
	dept_no TEXT,
	from_date DATE,
	to_date DATE,
	FOREIGN KEY (emp_no) REFERENCES Employees(emp_no)
);

CREATE TABLE IF NOT EXISTS Departments (
	dept_no TEXT,
	dept_name TEXT,
	PRIMARY KEY (dept_no)
);

COPY Employees FROM 'C:\Users\Nodak\Documents\GitHub\SQL_Challenge\Resources\employees.csv' DELIMITER ',' CSV HEADER;
COPY Salaries FROM 'C:\Users\Nodak\Documents\GitHub\SQL_Challenge\Resources\salaries.csv' DELIMITER ',' CSV HEADER;
COPY Titles FROM 'C:\Users\Nodak\Documents\GitHub\SQL_Challenge\Resources\titles.csv' DELIMITER ',' CSV HEADER;
COPY Dept_Emp FROM 'C:\Users\Nodak\Documents\GitHub\SQL_Challenge\Resources\dept_emp.csv' DELIMITER ',' CSV HEADER;
COPY Dept_Manager FROM 'C:\Users\Nodak\Documents\GitHub\SQL_Challenge\Resources\dept_manager.csv' DELIMITER ',' CSV HEADER;
COPY Departments FROM 'C:\Users\Nodak\Documents\GitHub\SQL_Challenge\Resources\departments.csv' DELIMITER ',' CSV HEADER;

