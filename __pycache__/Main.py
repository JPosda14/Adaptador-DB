# En el archivo main.py

from DBLogic import MySQLAdapter, CassandraAdapter

def main():
    # Configuración para MySQL
    mysql_config = {
        'host': 'localhost',
        'port': 3307,
        'user': 'root',
        'password': 'cue',
        'database': 'adapter_prove'
    }

    # Configuración para Cassandra
    cassandra_config = {
        'contact_points': ['localhost'],
        'port': 9042,
        'keyspace': 'prove_adapter'
    }

    # Crear instancias de adaptadores
    mysql_adapter = MySQLAdapter(**mysql_config)
    cassandra_adapter = CassandraAdapter(**cassandra_config)

    try:
        # Conectar a las bases de datos
        mysql_adapter.connect()
        cassandra_adapter.connect()

        # Ejemplo de operaciones en MySQL
        print("Operaciones en MySQL:")
        mysql_query = "SELECT * FROM players;"
        result = mysql_adapter.execute_query(mysql_query)
        print("Resultado de la consulta en MySQL:", result)

        # Ejemplo de actualización en MySQL
        mysql_update = "UPDATE players SET name = 'nuevo_nombre' WHERE id = 1;"
        mysql_adapter.execute_update(mysql_update)
        print("Actualización en MySQL realizada.")

        # Ejemplo de inserción en MySQL
        mysql_insert = "INSERT INTO players (name) VALUES ('nuevo_jugador');"
        mysql_adapter.execute_insert(mysql_insert)
        print("Inserción en MySQL realizada.")

        # Ejemplo de operaciones en Cassandra
        print("\nOperaciones en Cassandra:")
        cassandra_query = "SELECT * FROM players;"
        result = cassandra_adapter.execute_query(cassandra_query)
        print("Resultado de la consulta en Cassandra:", result)

        # Ejemplo de actualización en Cassandra
        cassandra_update = "UPDATE players SET name = 'nuevo_nombre' WHERE id = 1;"
        cassandra_adapter.execute_update(cassandra_update)
        print("Actualización en Cassandra realizada.")

        # Ejemplo de inserción en Cassandra
        cassandra_insert = "INSERT INTO players (id, name) VALUES (4, 'nuevo_jugador');"
        cassandra_adapter.execute_insert(cassandra_insert)
        print("Inserción en Cassandra realizada.")

    finally:
        # Cerrar conexiones
        mysql_adapter.close()
        cassandra_adapter.close()

if __name__ == "__main__":
    main()