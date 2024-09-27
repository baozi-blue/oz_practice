-- 9/26 수업내용 메모

-- CREATE DATABASE mydatabase; -- database 생성 
-- SHOW DATABASES;
-- USE mydatabase;
-- DROP DATABASE IF EXISTS mydatabase;

-- USE mysql;
-- CREATE USER 'username'@'localhost' IDENTIFIED BY 'oz-password';
-- SELECT * FROM user;
-- SHOW GRANTS FOR 'username'@'localhost';
-- SHOW GRANTS;

-- DROP USER 'username'@'localhost';
-- SELECT * FROM user;   -- 삭제됐는지 재확인

-- CREATE DATABASE testdatabase;
-- USE testdatabase;

-- CREATE TABLE users(
-- id INT auto_increment KEY,
--    username VARCHAR(30) NOT NULL,
--    email VARCHAR(100) UNIQUE,
--    is_business VARCHAR(10) DEFAULT False,
--    age INT CHECK (age >= 10)
-- );

-- CREATE TABLE users_2(
-- user_id INT PRIMARY KEY,
-- name VARCHAR(100),
--        age INT
-- );

-- INSERT INTO users_2(user_id, name, age)
-- VALUES (1, 'Alice', 25),
--       (2, 'Bob', 30),
--       (3, 'Charlie', 22),
--       (4, 'David', 33),
--       (5, 'Eve', 28);
  

-- CREATE TABLE orders (
-- order_id INT PRIMARY KEY,
-- user_id INT,
-- order_date DATE
-- );



-- 주석처리 단축키: command + /

-- INSERT INTO orders (order_id, user_id, order_date) 
-- VALUES (101, 1, '2023-01-01'),
--        (102, 2, '2023-02-01'),
-- 	      (103, 1, '2023-02-15'),
--        (104, 3, '2023-03-01'),
--        (105, 4, '2023-03-10'); 
       

------------------------------------------------------
-- 9/27 수업내용
-- USE testdatabase;
-- CREATE TABLE users (
--     user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
--     username TEXT NOT NULL,
--     email TEXT NOT NULL,
--     age INT

-- );

-- CREATE TABLE orders (
--     user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
--     product_name TEXT NOT NULL,
--     quantity INT
-- );



--------------------------------------------------------------------
-- 9/27 과제
# emplyees table 생성
-- CREATE TABLE employees (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(100),
--     position VARCHAR(100),
--     salary DECIMAL(10, 2)
-- );

# 직원 데이터 추가
-- INSERT INTO employees (name, position, salary) VALUES ('혜린', 'PM', 90000);
-- INSERT INTO employees (name, position, salary) VALUES ('은우', 'Frontend', 80000);
-- INSERT INTO employees (name, position, salary) VALUES ('가을', 'Backend', 92000);
-- INSERT INTO employees (name, position, salary) VALUES ('지수', 'Frontend', 78000);
-- INSERT INTO employees (name, position, salary) VALUES ('민혁', 'Frontend', 96000);
-- INSERT INTO employees (name, position, salary) VALUES ('하온', 'Backend', 130000);

# 직원의 이름과 연봉정보만 조회하는 쿼리 작성
-- SELECT name, salary FROM employees;

# frontend 직책 / 연봉 <= 90000  인 직원 조회
-- SELECT name, salary FROM employees WHERE position = 'Frontend' AND salary <= 90000;

# PM 직책 연봉 10% 인상 후 결과 확인
-- SET SQL_SAFE_UPDATES = 0;     # safe update mode off
-- UPDATE employees SET salary = salary * 1.10 WHERE position = 'PM';
-- SELECT * FROM employees WHERE position = 'PM';

# 백엔드 직원 연봉 5% 인상
-- UPDATE employees SET salary = salary * 1.05 WHERE position = 'Backend';

# '민혁'님 삭제
-- DELETE FROM employees WHERE name = '민혁';

# 직책별 평균 연봉 계산
-- SELECT position, AVG(salary) AS average_salary FROM employees GROUP BY position;

# employees table 삭제
-- DROP TABLE employees;





       
       
       
       
       