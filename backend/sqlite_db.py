import sqlite3


class DBConnection:
    '''This class will make calls to databse. Here in db_path variable will be provided as parameter
    on creation of the database'''
    
    def __init__(self, db_name: str) -> None:
        self.set_db_name(db_name)
        self.init_table()

    def set_db_name(self, db_name: str) -> None:
        self.db_name = db_name

    def get_db_name(self) -> str:
        return self.db_name

    def init_table(self) -> None:
        query = f'create table if not exists {self.get_db_name()[0:len(self.get_db_name()) - 3]} ' \
        '(id integer primary key autoincrement,'\
        'date varchar(10),'\
        'name varchar(255),'\
        'link varchar(255),'\
        'labels varchar(500),'\
        'content varchar(10000));'
        self.execute(query=query)

    def insert(self, query_values:dict) -> None:
        for item in query_values:
            print(item)
            print(type(item))
        query = f'insert into {self.get_db_name()[0:len(self.get_db_name()) - 3]} (date, name, link, labels, content) values (?, ?, ?, ?, ?);'
        query_params =  (query_values["date"],  query_values["name"], query_values["link"], query_values["labels"], query_values["content"])
        self.execute(query = query, params = query_params)


    def execute(self, query, params = ()) -> None:
        print(query)
        connection = sqlite3.connect(self.get_db_name())
        cursor = connection.cursor()

        cursor.execute(query, params)
        
        connection.commit()
        connection.close()



    