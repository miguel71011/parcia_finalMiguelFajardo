import mariadb
config = {
    'host': 'localhost',
    'port': 3308,
    'user': 'root',
    'password': '',
    'database': 'control'
}
DB = mariadb.connect(**config)
DB.autocommit = True
