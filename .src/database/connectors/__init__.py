from django.conf import settings
from django.db import connections

def get_database_connection():
    """
    Retrieves a database connection based on the settings configuration.
    :return: Database connection object
    """
    try:
        database_name = settings.DATABASES['default']['NAME']
        connection = connections[database_name]
        return connection
    except KeyError:
        raise KeyError("Database configuration does not exist.")
    except Exception as e:
        raise Exception("Error while connecting to the database: {}".format(str(e)))

def close_database_connection():
    """
    Closes the database connection.
    """
    connection = get_database_connection()
    connection.close()

def test_database_connection():
    """
    Tests the database connection by establishing a connection and checking if it is not None.
    """
    connection = get_database_connection()
    if connection is None:
        raise Exception("Failed to establish a database connection.")