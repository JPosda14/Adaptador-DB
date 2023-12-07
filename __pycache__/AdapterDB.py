# En el archivo DBLogic.py

import mysql.connector
from cassandra.cluster import Cluster

class Database:
    def connect(self):
        pass

    def execute_query(self, query, data=None):
        pass

    def execute_update(self, query, data=None):
        pass

    def close(self):
        pass

    def clone(self):
        pass

class MySQLAdapter(Database):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
    
    def clone(self):
        return MySQLAdapter(self.host, self.port, self.user, self.password, self.database)

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, data=None):
        self.cursor.execute(query, data)
        return self.cursor.fetchall()

    def execute_update(self, query, data=None):
        self.cursor.execute(query, data)
        self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()
        if self.cursor:
            self.cursor.close()

class CassandraAdapter(Database):
    def __init__(self, contact_points, keyspace, port):
        self.contact_points = contact_points
        self.keyspace = keyspace
        self.port = port
        self.cluster = None
        self.session = None

    def connect(self):
        self.cluster = Cluster(contact_points=self.contact_points, port=self.port)
        self.session = self.cluster.connect(keyspace=self.keyspace)

    def execute_query(self, query, data=None):
        return self.session.execute(query, data)

    def execute_update(self, query, data=None):
        self.session.execute(query, data)

    def close(self):
        if self.cluster:
            self.cluster.shutdown()