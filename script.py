#converts .csv to .sql

import pandas as pd 
import mariadb
import sys

chunksize = 10 ** 6

conn = mariadb.connect(
    user="sociedatos",
    password="123",
    host="127.0.0.1",
    database="LINKEDIN"
    )

conn.autocommit = False

def filter_locality(value):
    try:
        return value.split(',')[0]
    except:
        return None

def filter_integers(value):
    try:
        if str(value) != 'nan':
            value = int(float(str(value)))
            return value if value < 2021 else None
        else:
            return None
    except:
        return None

def filter_str(value):
    try:
        if str(value) != 'nan':
            return eval("b'"+str(value)+"'").decode('utf-8')
        else:
            return None
    except:
        return None

def mariadb_insert(row):
    cur = conn.cursor()
    cur.execute("INSERT INTO companies (company_url_domain, company_name, country, industry, linkedin_url, locality, total_employee_estimate, year_founded) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (filter_str(row['Company URL domain']), filter_str(row['Company name']), filter_str(row['Country']), filter_str(row['Industry']), filter_str(row['Linkedin URL']), filter_str(row['Locality']), filter_integers(row['Total employee estimate']), filter_integers(row['Year founded'])))
    conn.commit()

def process(chunk):
    chunk = chunk[chunk['Country'].notnull()] # not null
    locality_chunk = chunk['Locality'].apply(lambda e : filter_locality(e))
    chunk.update(locality_chunk)
    chunk.apply(lambda row : mariadb_insert(row), axis = 1)

for chunk in pd.read_csv('companies-on-linkedin.csv', delimiter=';', skiprows=0, chunksize=chunksize):
    process(chunk)


