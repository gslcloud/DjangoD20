import psycopg2

class PostgreSQLConnector:
    def __init__(self):
        pass

    def connect(self, host, port, dbname, user, password):
        if not all((host, port, dbname, user, password)):
            raise ValueError("Missing database credentials")

        try:
            connection = psycopg2.connect(
                host=host,
                port=port,
                dbname=dbname,
                user=user,
                password=password
            )
            return connection
        except psycopg2.Error as e:
            raise Exception(f"Error connecting to the PostgreSQL database: {e}")

    def execute_query(self, connection, query):
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            connection.commit()
            return results
        except psycopg2.Error as e:
            raise Exception(f"Error executing SQL query: {e}")