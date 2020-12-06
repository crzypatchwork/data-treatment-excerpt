
CREATE DATABASE LINKEDIN;

CREATE USER 'sociedatos'@'localhost' IDENTIFIED BY '123';
GRANT ALL PRIVILEGES ON *.* TO 'sociedatos'@'localhost' IDENTIFIED BY '123';

USE LINKEDIN;

CREATE TABLE companies (
	id INT AUTO_INCREMENT PRIMARY KEY,
    company_url_domain VARCHAR(100),
    company_name VARCHAR(100),
    country VARCHAR(100),
    industry VARCHAR(100),
    linkedin_url VARCHAR(100),
    locality VARCHAR(100),
    total_employee_estimate INT,
    year_founded YEAR
);