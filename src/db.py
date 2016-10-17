import psycopg2
import psycopg2.pool
import os


class Database:
    def __init__(self):
        #self.pool = psycopg2.pool.ThreadedConnectionPool(1, 5, host=os.getenv('DBHOST', 'localhost'), port=os.getenv('DBPORT', '5432'), user=os.getenv('DBUSER','stop'), database=os.getenv('DBNAME','stop'), password=os.getenv('DBPASS','stop'))
        self.pool = psycopg2.pool.ThreadedConnectionPool(1, 5, host=os.getenv('DBHOST', 'ec2-54-217-213-156.eu-west-1.compute.amazonaws.com'), port=os.getenv('DBPORT', ''), user=os.getenv('DBUSER', 'hqcqeccowirrxj'), database=os.getenv('DBNAME', 'd8r79ti4iuqq79'),
    password=os.getenv('DBPASS', 'Cf5uDO5AbUeExQz5a6KWSjnKDF'))

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

