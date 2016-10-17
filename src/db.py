import asyncio
import time
import psycopg2
import psycopg2.pool
import os

import sys


class Database:
    def __init__(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.init_connection())
    
    @asyncio.coroutine
    def init_connection(self):
        result = 1
        loop_end = time.time() + 10
        while time.time() < loop_end:
            try:
                self.pool = psycopg2.pool.ThreadedConnectionPool(1, 5, host=os.getenv('DBHOST', 'localhost'),
                                                                 port=os.getenv('DBPORT', '5432'),
                                                                 user=os.getenv('DBUSER', 'stop'),
                                                                 database=os.getenv('DBNAME', 'stop'),
                                                                 password=os.getenv('DBPASS', 'stop'))
                result = 0
                break
            except:
                continue
        if result:
            print ("Initializing a database connection failed")
            sys.exit()
    
    def get_connection(self):
        return self.pool.getconn()
    
    def put_connection(self, conn):
        self.pool.putconn(conn)
    
    def store_request(self, trip_id, stop_id):
        conn = self.get_connection()
        cur = conn.cursor()
        values = (trip_id, stop_id)
        sql = "INSERT INTO request (trip_id, stop_id, user_id, req_time) VALUES (%s, %s, 'user', now())"
        cur.execute(sql, values)
        conn.commit()
        self.put_connection(conn)

