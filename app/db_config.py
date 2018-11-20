import os
import psycopg2

url = os.getenv('DATABASE_URI')

def connection(url):
    """
    function to establish connection to postgres using a psycopg2 adapter
    """
    con = psycopg2.connect(url)
    return con

def init_db():
    """
    make the connection function available to external modules
    """
    con = connection(url)
    return con
def create_tables():
    """
    initializes the tables in the sendIT database
    """
    conn = connection(url)
    curr = conn.cursor()
    executable = tables()

    for query in executable:
        curr.execute(query)
    conn.commit()
def destroy_tables():
    pass

def tables():
    """
    function contains the query strings to create tables in the database
    """
    db1 = """CREATE TABLE IF NOT EXISTS orders (
        order_id serial PRIMARY KEY NOT NULL,
        user_id numeric NOT NULL,
        item_name character varying(50) NOT NULL,
        pickup_location character varying(50) NOT NULL,
        destination character varying(50) NOT NULL,
        pricing numeric NOT NULL,
        status character varying(10)
        )"""
    
    db2 = """CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY NOT NULL,
        email character varying(50) NOT NULL,
        role character varying(50),
        password character varying(50) NOT NULL
        )"""

    queries = [db1, db2]
    return queries
