import MySQLdb

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '',
    'db': 'fastapi_demo',
}

# Create a connection to the database
conn = MySQLdb.connect(**db_config)