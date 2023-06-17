from getpass import getpass


def config_db_init():
    host = 'localhost'
    user = input('Enter the database server login: ')
    password = getpass('Enter the database server password: ')
    database = 'Human_friends'
    return [host, user, password, database]