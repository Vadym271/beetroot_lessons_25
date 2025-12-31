SELECT first_name, last_name FROM employees;
SELECT employee_id, department_id FROM employees;
SELECT * FROM employees ORDER BY first_name DESC;
SELECT first_name, last_name, salary, salary * 0.12 as PF FROM employees;
SELECT MAX(salary) as max_salary, MIN(salary) as min_salary FROM employees;
SELECT first_name, last_name, Round(salary *1.0 / 12, 2) FROM employees;
