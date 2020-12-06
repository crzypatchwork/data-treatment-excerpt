CREATE DATABASE LINKEDIN;

CREATE USER 'sociedatos'@'localhost' IDENTIFIED BY '123';
GRANT ALL PRIVILEGES ON *.* TO 'sociedatos'@'localhost' IDENTIFIED BY '123';

USE LINKEDIN;

ALTER DATABASE LINKEDIN CHARACTER SET 'utf8' COLLATE 'utf8_unicode_ci';

CREATE TABLE companies (
	id INT AUTO_INCREMENT PRIMARY KEY,
    company_url_domain VARCHAR(100),
    company_name VARCHAR(512) CHARACTER SET utf8 COLLATE utf8_unicode_ci,
    country VARCHAR(100),
    industry VARCHAR(100),
    linkedin_url VARCHAR(200),
    locality VARCHAR(100),
    total_employee_estimate INT,
    year_founded INT
) CHARACTER SET utf8 COLLATE utf8_unicode_ci;

select * from companies limit 10;
drop table companies;

# https://github.com/bahar/WorldCityLocations/blob/master/World_Cities_Location_table.sql

select corp.locality, loc.latitude, loc.longitude from location as loc
join companies as corp
on corp.locality = loc.city;