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
                self.pool = psycopg2.pool.ThreadedConnectionPool(1, 20, host=os.getenv('DBHOST', 'localhost'),
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
    
    def store_request(self, trip_id, stop_id, device_id, push_notification):
        conn = self.get_connection()
        cur = conn.cursor()
        if device_id == '0':
            values = (trip_id, stop_id, device_id, True)
        else:
            values = (trip_id, stop_id, device_id, not push_notification)
        sql = "INSERT INTO request (trip_id, stop_id, user_id, device_id, pushed, req_time, canceled) VALUES (%s, %s, 'user', %s, %s, now(), false) RETURNING id"
        cur.execute(sql, values)
        request_id = cur.fetchone()[0]
        conn.commit()
        self.put_connection(conn)
        return request_id
    
    def get_request_info(self, request_id):
        conn = self.get_connection()
        cur = conn.cursor()
        values = (request_id,)
        sql = "SELECT trip_id, stop_id FROM request WHERE id = %s"
        cur.execute(sql, values)
        result = cur.fetchone()
        self.put_connection(conn)
        return result

    def cancel_request(self, request_id):
        conn = self.get_connection()
        cur = conn.cursor()
        values = (request_id,)
        sql = "UPDATE request SET canceled = true, cancel_time = now() WHERE id = %s RETURNING trip_id"
        cur.execute(sql, values)
        trip_id = cur.fetchone()[0]
        conn.commit()
        self.put_connection(conn)
        return trip_id
        
    def get_requests(self, trip_id):
        conn = self.get_connection()
        cur = conn.cursor()
        values = (trip_id,)
        sql = "SELECT stop_id FROM request WHERE canceled = false AND trip_id = %s"
        cur.execute(sql, values)
        result = cur.fetchall()
        self.put_connection(conn)
        return result

    def store_report(self, trip_id, stop_id):
        conn = self.get_connection()
        cur = conn.cursor()
        values = (trip_id, stop_id)
        sql = "INSERT INTO report (trip_id, stop_id, user_id, report_time) VALUES (%s, %s, 'user', now())"
        cur.execute(sql, values)
        conn.commit()
        self.put_connection(conn)
    
    def get_unpushed_requests(self):
        conn = self.get_connection()
        cur = conn.cursor()
        sql = "SELECT trip_id,id,stop_id,device_id FROM request WHERE canceled = false AND pushed = false"
        cur.execute(sql)
        result = cur.fetchall()
        self.put_connection(conn)
        return result
    
    def set_pushed(self, ids):
        conn = self.get_connection()
        cur = conn.cursor()
        values = (tuple(ids),)
        sql = "UPDATE request SET pushed = true WHERE id IN %s"
        cur.execute(sql, values)
        conn.commit()
        self.put_connection(conn)
