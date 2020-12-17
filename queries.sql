
USE LINKEDIN;

SELECT * FROM industries_count ORDER BY count DESC;

alter table industries_count change column I industry VARCHAR(100);
alter table industries_count change column `(SELECT COUNT(industry) FROM companies WHERE industry=I)` `count` INT;

SELECT * FROM companies LIMIT 10;

SELECT DISTINCT COUNT(country), country FROM companies WHERE country IN (SELECT DISTINCT country FROM companies);

(SELECT COUNT(country) FROM companies WHERE country = 'united states');

CREATE TABLE countries_count AS SELECT DISTINCT country AS C, (SELECT COUNT(country) FROM companies WHERE country = C) FROM companies;

alter table countries_count change column C country VARCHAR(100);
alter table countries_count change column `(SELECT COUNT(country) FROM companies WHERE country = C)` `count` INT;

CREATE VIEW countries_counter AS
select * from countries_count;

select corp.company_name, corp.locality, loc.latitude, loc.longitude from location as loc
join companies as corp
on corp.locality = loc.city;

CREATE TABLE industries_count AS SELECT DISTINCT industry AS I, (SELECT COUNT(industry) FROM companies WHERE industry=I) FROM companies;
CREATE TABLE industries_regions_count AS SELECT DISTINCT country AS C, industry AS I, (SELECT COUNT(industry) FROM companies WHERE industry=I AND country=C) FROM companies;

alter table industries_count change column I industry VARCHAR(100);
alter table industries_count change column `(SELECT COUNT(industry) FROM companies WHERE industry=I)` `count` INT;

select * from countries_count order by count desc limit 10;

/*
DELIMITER $$
create procedure country_latlong (country VARCHAR(100))
BEGIN
select corp.company_name, corp.locality, loc.latitude, loc.longitude from location as loc
join companies as corp
on corp.country = country;
END $$
DELIMITER;
*/

call country_latlong('brazil');

/*
DELIITER $$
create procedure get_company (company VARCHAR(100))
BEGIN
select * from companies on corp.company_name = company;
END$$
DELIMITER;
*/

select * from companies where country = 'brazil' order by cast(total_employee_estimate as int) asc limit 100;

