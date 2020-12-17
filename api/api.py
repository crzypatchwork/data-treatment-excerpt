
from flask import Flask, request
import mariadb
from libs import validate

app = Flask(__name__)
v = validate()

conn = mariadb.connect(
    user="sociedatos",
    password="123",
    host="127.0.0.1",
    database="LINKEDIN"
    )

conn.autocommit = False

@app.route('/countries_count', methods=['GET'])
def get_countries_count():
    
    cursor = conn.cursor()
    cursor.execute('select * from countries_count order by count desc')
    records = cursor.fetchall()

    aux_arr = [{'country' : e[0], 'count': e[1]} for e in records] if request.args.get('size') == None else [{'country' : e[0], 'count': e[1]} for e in records][:int(request.args.get('size'))]

    return { 'payload' : aux_arr , 'length' : aux_arr.__len__() }

@app.route('/industries_count', methods=['GET'])
def get_industries_count():

    cursor = conn.cursor()
    cursor.execute('select * from industries_count order by count desc')
    records = cursor.fetchall()

    aux_arr = [{'industry' : e[0], 'count': e[1]} for e in records] if request.args.get('size') == None else [{'industry' : e[0], 'count': e[1]} for e in records][:int(request.args.get('size'))]

    return { 'payload' : aux_arr , 'length' : aux_arr.__len__() }

@app.route('/country_coordinates', methods=['POST'])
def country_coordinates():

    payload = v.read_requests(request)
    return { 'status' : 200 }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

