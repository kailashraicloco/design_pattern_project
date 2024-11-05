from database_layer.database_connection import DatabaseConnection
def connect_to_db():
    new_connection = DatabaseConnection()
    newer_connection = DatabaseConnection()
    print(new_connection is newer_connection)



if __name__ == '__main__':
    connect_to_db()
