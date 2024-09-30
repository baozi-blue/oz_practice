-- USE classicmodels; 

-- SELECT CustomerName FROM customers;

-- SELECT * FROM products
-- WHERE productLine = 'Classic Cars';

-- SELECT * from orders ORDER BY orderDate DESC LIMIT 10;


-- SELECT * FROM payments WHERE amount >= 100;

-- SELECT o.orderNumber, c.customerName
-- FROM orders o 
-- JOIN customers c ON o.customerNumber = c.customerNumber;



-- 필요한 데이터 가져올 때
-- SELECT p.productName, p.productLine, pl.textDescription
-- FROM products p
-- JOIN productlines pl ON p.productLine = pl.productLine;



-- 전체 데이터 가져올때
-- SELECT p.*, pl.*
-- FROM products p
-- JOIN productlines pl ON p.productLine = pl.productLine;


-- SELECT e1.employeeNumber, e1.firstName, e1.lastName, e2.firstName AS 'ManagerFirstName', e2.lastName AS 'ManagerLastName'
-- FROM employees e1
-- LEFT JOIN employees e2 ON e1.reportsTo = e2.employeeNumber;


-- SELECT e.employeeNumber, e.lastName, e.firstName, e.extension, e.email, e.officeCode, e.reportsTo, e.jobTitle
-- FROM employees e
-- JOIN offices o ON e.officeCode = o.officeCode
-- WHERE o.city = 'San Francisco'




-- 제품 카테고리별 수량
-- SELECT productLine, COUNT(*) AS productCount
-- FROM products
-- GROUP BY productLine;




-- 고객 주문 총금액
-- SELECT customers.customerNumber,
--        customers.customerName,
--        SUM(orderdetails.quantityOrdered * orderdetails.priceEach) AS totalAmoumt
-- FROM customers
-- JOIN orders ON customers.customerNumber = orders.customerNumber
-- JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
-- GROUP BY customers.customerNumber, customers.customerName;



-- 가장 많이 판매된 제품
-- SELECT productName, SUM(quantityOrdered) AS totalQuantity
-- FROM orderdetails od
-- JOIN products p ON od.productCode = p.productCode
-- GROUP BY productName
-- ORDER BY totalQuantity DESC
-- LIMIT 1;



-- 매출 가장 많은 지역
-- SELECT o.city, SUM(od.quantityOrdered * od.priceEach) AS totalSales
-- FROM orders ord
-- JOIN orderdetails od ON ord.orderNumber = od.orderNumber
-- JOIN customers c ON ord.customerNumber = c.customerNumber
-- JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber
-- JOIN offices o ON e.officeCode = o.officeCode
-- GROUP BY o.city
-- ORDER BY totalSales DESC
-- LIMIT 1;





-- 500불 이상의 주문
-- SELECT orderNumber, SUM(quantityOrdered * priceEach) AS totalAmount
-- FROM orderdetails
-- GROUP BY orderNumber
-- HAVING totalAmount > 500;





-- 평균 주문 금액 이상인 고객 (틀렸음? payments 내 같은 고객 두건 이상 주문 있을 수 있음)
-- SELECT customerNumber, SUM(amount) AS totalPayment
-- FROM payments
-- GROUP BY customerNumber
-- HAVING totalPayment > (SELECT AVG(amount) FROM payments);





-- 주문 없는 고객
-- SELECT customerName
-- FROM customers
-- WHERE customerNumber NOT IN (SELECT customerNumber FROM orders);




-- 가장 많이 구매한 고객 (VIP고객)
-- SELECT c.customerName, SUM(od.quantityOrdered * od.priceEach) AS totalSpent
-- FROM customers c
-- JOIN orders o ON c.customerNumber = o.customerNumber
-- JOIN orderdetails od ON o.orderNumber = od.orderNumber
-- GROUP BY c.customerName
-- ORDER BY totalSpent DESC
-- LIMIT 1;



-- # 데이터 수정 및 관리 
-- 신규 고객 추가 i.e.
-- INSERT INTO customers (customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
-- VALUES ('New Customer', 'Lastname', 'Firstname', '123-456-7890', '123 Street', 'Suite 1', 'City', 'State', 'PostalCode', 'Country', 1002, 50000.00);



-- 제품 가격 변경
-- UPDATE products
-- SET buyPrice = buyPrice * 1.10
-- WHERE productLine = 'Classic Cars';customers


-- 고객 정보 변경
-- UPDATE customers
-- SET email = 'newemail@example.com'
-- WHERE customerNumber = 103;

-- 직원 정보 업데이트
-- UPDATE employees
-- SET officeCode = 'New York'
-- WHERE employeeNumber = 1002;




-- # ERD (Entity Relationship Diagram) 프로그램
-- # 데이터베이스 구조를 시각적으로 표현하는 도구: Aquery, MySQL Workbench, Draw.io(diagrams.net)


































































