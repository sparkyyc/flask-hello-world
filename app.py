import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Christa Sparks in 3308'

@app.route('/db_test')
def db_test():
   conn = psycopg2.connect("postgresql://sparkyyc_db_user:v0J6Bm3YGWmxYFcWuSmckXaRXohUyh3P@dpg-cqk3hujqf0us73c29050-a/sparkyyc_db")
   conn.close()
   return 'Database connection successful'

@app.route('/db_create')
def db_create():
   conn = psycopg2.connect("postgresql://sparkyyc_db_user:v0J6Bm3YGWmxYFcWuSmckXaRXohUyh3P@dpg-cqk3hujqf0us73c29050-a/sparkyyc_db")
   cur = conn.cursor()
   cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
   conn.commit()
   conn.close()
   return 'Basketball Table created successfully'

@app.route('/db_insert')
def db_insert():
   conn = psycopg2.connect("postgresql://sparkyyc_db_user:v0J6Bm3YGWmxYFcWuSmckXaRXohUyh3P@dpg-cqk3hujqf0us73c29050-a/sparkyyc_db")
   cur = conn.cursor()
   cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
   conn.commit()
   conn.close()
   return 'Basketball Table Populated'