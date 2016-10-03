import psycopg2
import psycopg2.pool
import os


class Database:
    def __init__(self):
        self.pool = psycopg2.pool.ThreadedConnectionPool(1, 5, host=os.getenv('DBHOST', 'ec2-54-217-213-156.eu-west-1.compute.amazonaws.com'), port=os.getenv('DBPORT', ''), user=os.getenv('DBUSER','hqcqeccowirrxj'), database=os.getenv('DBNAME','d8r79ti4iuqq79'), password=os.getenv('DBPASS','Cf5uDO5AbUeExQz5a6KWSjnKDF'))

    def get_connection(self):
        return self.pool.getconn()
    
    def put_connection(self, conn):
        self.pool.putconn(conn)
    
    def default(self):
        conn = self.get_connection()
        # conn.execute("SQL")
        conn.commit()
        self.put_connection(conn)

