use my_db;

create table employees (
emp_id INT PRIMARY KEY,
emp_name VARCHAR(100),
department VARCHAR(50),
salary DECIMAL(10,2),
joining_date DATE
);

create table projects (
project_id INT PRIMARY KEY,
project_name VARCHAR(100),
start_date DATE,
end_date DATE
);

create table employee_project (
emp_id INT,
project_id INT, 
hours_worked INT,
rating INT,
PRIMARY KEY(emp_id, project_id),
FOREIGN KEY(emp_id) REFERENCES employees(emp_id),
FOREIGN KEY(project_id) REFERENCES projects(project_id)
);

INSERT INTO employees VALUES
(1,'Vips','IT',70000,'2022-01-10'),
(2,'Vishal','HR',30000,'2021-01-10'),
(3,'Ayush','Design',34000,'2019-01-10'),
(4,'Vivek','Dev',50000,'2024-01-10'),
(5,'Shamish','Finance',20000,'2023-01-10'),
(6,'Samy','Finance',20000,'2026-01-10');


select * from employees;

INSERT INTO projects VALUES
(1012,'AI Bot','2022-01-10','2023-01-10'),
(1013,'Website Design','2021-01-10','2022-01-10'),
(1014,'Application Work','2019-01-10','2020-01-10'),
(2102,'Database Migration','2024-01-10','2025-01-10');

select * from projects;

INSERT INTO employee_project VALUES
(1,1012,120,5),
(1,1013,90,4),
(2,1012,80,4),
(3,1013,50,5),
(2,2102,20,3),
(4,2102,150,5),
(5,1012,40,4),
(3,1014,120,4);

INSERT INTO employee_project VALUES
(3,1012,120,5),
(4,1013,90,4);

select * from employee_project;

select e.emp_id,e.emp_name
from employees e
join employee_project ep
on e.emp_id=ep.emp_id
group by e.emp_id,e.emp_name
having COUNT(ep.project_id) > 2;

select e.emp_id, e.emp_name, AVG(ep.rating) AS avg_rating
from employees e 
join employee_project ep
on e.emp_id=ep.emp_id
group by e.emp_id,e.emp_name
having AVG(ep.rating) > 4;

select * 
from employees e
where salary = (
select MAX(salary)
from employees
where department=e.department
);

select * 
from employees e
where e.emp_id NOT IN(
select emp_id
from employee_project
);

select p.project_id,p.project_name, SUM(ep.hours_worked) as total_hours
from projects p
join employee_project ep
on p.project_id=ep.project_id
group by p.project_id,p.project_name
order by total_hours desc 
limit 1;

#2

create table customers(
customer_id INT PRIMARY KEY,
name VARCHAR(100),
city VARCHAR(50)
);

create table orders(
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE, 
total_amount DECIMAL(10,2),
FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

create table order_items(
order_item_id INT PRIMARY KEY,
order_id INT,
product_id INT, 
qunatity INT,
FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

create table products(
product_id INT PRIMARY KEY,
product_name VARCHAR(100),
price DECIMAL(10,2)
);

INSERT INTO customers VALUES
(1,'Vips','Delhi'),
(2,'Vishal','Mumbai'),
(3,'Abhishek','Pune'),
(4,'Shardha','Bangalore');

INSERT INTO products VALUES
(101,'Laptop',75000),
(102,'Phone',50000),
(103,'Headphones', 500),
(104,'Keyboard',1500);

INSERT INTO orders VALUES
(1,1,'2024-05-10',75000),
(2,4,'2024-05-10',1500),
(3,2,'2024-07-10',50000),
(4,3,'2024-09-10',500),
(5,1,'2024-06-10',500),
(6,1,'2024-10-10',50000);

INSERT INTO order_items VALUES
(1,1,101,1),
(2,2,104,1),
(3,3,102,1),
(4,4,103,1),
(5,5,103,1),
(6,6,102,1);

select c.customer_id,c.name
from customers c
join orders o
on c.customer_id=o.customer_id
group by c.customer_id,c.name
having count(o.order_id) >2;

select c.customer_id,c.name, SUM(o.total_amount) as total_spent
from customers c
join orders o
on c.customer_id=o.customer_id
group by c.customer_id,c.name
order by total_spent desc
limit 5;

select p.product_id, p.product_name, SUM(oi.qunatity) as total_ordered
from products p
join order_items oi
on p.product_id=oi.product_id
group by p.product_id,p.product_name
order by total_ordered desc
limit 1;

select * 
from customers c
left join orders o 
on c.customer_id=o.customer_id
where o.order_id is NULL;

select year(order_date) as year, month(order_date) as month, sum(total_amount) as revenue
from orders 
group by year(order_date), month(order_date) 
order by year, month;

#3

select * 
from employees 
where salary > (
select AVG(salary)
from employees
);

select * 
from employees e 
where salary > (
select AVG(salary)
from employees
where department = e.department
);

select * 
from employees e 
where salary = (
select MAX(salary)
from employees
where department=e.department
);

select * from employees where salary > (select avg(salary) from employees) and salary < (select max(salary) from employees);

select department
from employees 
group by department 
having avg(salary) > (
select avg(salary)
from employees
);

#4

select customer_id, sum(total_amount) as total_spent
from orders
group by customer_id;

select customer_id, count(order_id) as total_orders
from orders
group by customer_id;

select customer_id, count(order_id) as total_orders
from orders 
group by customer_id
having count(order_id) > 2;

select customer_id, sum(total_amount) as total_spent 
from orders
group by customer_id
having sum(total_amount) > 10000;

select product_id, sum(qunatity) as total_quantity
from orders
group by product_id
having sum(qunatity) > 100;