import pyodbc

class DatabaseManager:
    __DRIVER = "{SQL SERVER}"
    __DATABASE = "db_library"
    __SERVER = "localhost"

    conn = None
    cursor = None

    @classmethod
    def get_connection(cls) -> pyodbc.Connection:
        if not cls.conn:
            cls.conn = pyodbc.connect(f"DRIVER={cls.__DRIVER};SERVER={cls.__SERVER};DATABASE={cls.__DATABASE};Trusted_Connection=Yes")
        return cls.conn
    
    @classmethod
    def get_cursor(cls) -> pyodbc.Cursor:
        return cls.get_connection().cursor()