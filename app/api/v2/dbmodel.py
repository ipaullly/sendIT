import os
import psycopg2
from psycopg2.extras import RealDictCursor

class SenditDb():
    """
    contains methods that perform query string operations on the databaes
    """
    @classmethod
    def start_db(cls, uri):
        """
        method to initialize the database
        """
        cls.conn = psycopg2.connect(uri)
        cls.cur = cls.conn.cursor(cursor_factory=RealDictCursor)

    @classmethod
    def build_all(cls):
        """
        method that creates the tables in the database
        """
        cls.cur.execute("""CREATE TABLE IF NOT EXISTS orders (
        order_id serial PRIMARY KEY NOT NULL,
        user_id numeric NOT NULL,
        item_name character varying(50) NOT NULL,
        pickup_location character varying(50) NOT NULL,
        destination character varying(50) NOT NULL,
        pricing numeric NOT NULL,
        status character varying(10)
        );
        CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY NOT NULL,
        email character varying(50) NOT NULL,
        role character varying(50),
        password character varying(50) NOT NULL
        )"""
        )
        cls.conn.commit()

    @classmethod
    def add_to_db(cls, query_string, tuple_data):
        """
        method that saves queries into the database
        """
        cls.cur.execute(query_string, tuple_data)
        cls.conn.commit()
    
    @classmethod
    def retrieve_one(cls, query_string, tuple_data):
        """
        method returns data on a particular row from the database
        """
        cls.cur.execute(query_string, tuple_data)
        return cls.cur.fetchone()

    @classmethod
    def retrieve_all(cls, query_string):
        """
        returns all specified columns from table rows
        """
        cls.cur.execute(query_string)
        return cls.cur.fetchall()
    
    @classmethod
    def drop_all(cls):
        """
        Destroys tables form the database
        """
        cls.cur.execute("""DROP TABLE IF EXISTS users CASCADE;\
        DROP TABLE IF EXISTS orders CASCADE;""")
        cls.conn.commit()
    