SELECT employees.first_name, employees.last_name, employees.department_id, department.department_name
FROM employees
JOIN department
on employees.department_id = department.department_id;


SELECT employees.first_name, employees.last_name, department.department_name, 
locations.city, locations.state_province
FROM employees

JOIN department
on employees.department_id = department.department_id

JOIN locations
on department.location_id = locations.location_id;


SELECT employees.first_name, employees.last_name, employees.department_id, department.department_name
FROM employees
JOIN department
on employees.department_id = department.department_id
WHERE department.department_id = 40 or department.department_id = 80;


SELECT department_name FROM department;

SELECT employees.first_name, managers.first_name 
FROM employees
JOIN employees managers
on employees.manager_id = managers.employee_id;

SELECT employees.first_name, employees.last_name, jobs.job_title, 
jobs.max_salary - employees.salary as sal_diff
FROM employees
join jobs
on employees.job_id = jobs.job_id;

SELECT jobs.job_title, avg(employees.salary) 
FROM employees
JOIN jobs
on employees.job_id = jobs.job_id
GROUP BY jobs.job_title;


SELECT employees.first_name, employees.last_name, employees.salary
FROM employees
JOIN department
on employees.department_id = department.department_id
JOIN locations
on department.location_id = locations.location_id
WHERE locations.city = 'London';


SELECT department.department_name, COUNT(*)
FROM employees
JOIN department
on employees.department_id = department.department_id
GROUP BY department.department_id;
