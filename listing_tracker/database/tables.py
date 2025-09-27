import listing_tracker.database.connection as connection

class Column: 
    def __init__(self, name: str, type: str, null: bool, default: str):
        self.name = name
        self.type = type
        self.null = "" if null else "NOT NULL"
        self.default = default
        self.statement= f'{self.name} {self.type} {self.null} {self.default}'

class Table:
    def __init__(self, name: str):
        self.name = name
        self.columns: list[Column] = []

    def assign_columns(self, columns: list[Column]):
        [self.columns.append(column) for column in columns]
    
    def exists(self):
        find = connection.cursor.execute(f'SELECT name FROM sqlite_master WHERE type="table" AND name="{self.name}";')
        exists = True if len(find.fetchall()) > 0 else False
        return exists
    
    def create(self):
        cursor_statement = f'CREATE TABLE {self.name}('
        for column in self.columns:
            cursor_statement += column.statement
            cursor_statement += ", " if column != self.columns[-1] else ")"
        connection.cursor.execute(cursor_statement)
    
    def insert(self, values: tuple):
        cursor_statement = f'INSERT INTO {self.name} VALUES{values};'
        connection.cursor.execute(cursor_statement)
        connection.db.commit()

    def insert_many(self, values: list[tuple]):
        cursor_statement = f'INSERT INTO {self.name} VALUES'
        for row in values:
            cursor_statement += f'{row}'
            cursor_statement += ", " if row != values[-1] else ";"
        connection.cursor.execute(cursor_statement)
        connection.db.commit()