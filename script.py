
import pandas as pd 
import mysql.connector
import sys

#CREATE USER 'sociedatos'@'localhost' IDENTIFIED BY '123';

try:
	conn = mysql.connector.connect(
    user="sociedatos",
    password="123",
    host="localhost",
    port=3306,
    database="LINKEDIN"
    )
except:
	print('err')
cur = conn.cursor()

df = pd.read_csv('../companies-on-linkedin.csv', delimiter=';', skiprows=0, low_memory=False)
df = df[df['Country'].notnull()] # not null

def filter_locality(value):
    try:
        print (value)
        return value.split(',')[1]
    except:
        pass

locality_df = df['Locality'].apply(lambda e : filter_locality(e))
df.update(locality_df)

def mariadb_insert(row):
	print(row)
	cursor.execute("INSERT INTO companies (company_url_domain, company_name, country, industry, linkedin_url, locality, total_employee_estimate, year_founded) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", 
(row['Company URL domain'], row['Company name'], row['Country'], row['Industry'], row['Linkedin URL'], row['Locality'], int(str(row['Total employee estimate'])), int(str(row['Year founded']))))

df.apply(lambda row : mariadb_insert(row))

conn.commit()


