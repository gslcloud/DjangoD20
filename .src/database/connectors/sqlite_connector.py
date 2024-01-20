import sqlite3
import logging

logger = logging.getLogger(__name__)

class SQLiteConnector:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.database_name)
            logger.info("Connected to database: %s", self.database_name)
        except sqlite3.Error as e:
            logger.error("Failed to connect to database: %s", self.database_name)
            raise ConnectionError(f"Failed to connect to database: {str(e)}")

    def close(self):
        if self.connection:
            self.connection.close()
            logger.info("Connection to database closed")
            self.connection = None

    def execute_query(self, query, parameters=None):
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(query, parameters)
                logger.info("Query executed successfully: %s", query)
                return cursor.fetchall()
        except sqlite3.Error as e:
            logger.error("Error executing query: %s", query)
            raise DatabaseError(f"Error executing query: {str(e)}")
