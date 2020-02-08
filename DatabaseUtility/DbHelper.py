import DB_Connector

class DbHelper:
    def __init__(self):
        self.cursor = DB_Connector.cursor

    def get_all_old_age(self):
        self.cursor.execute("select * from oldpeople")

    def get_all_young(self):
        self.cursor.execute("select * from youngpeople")

    def execute_query(self,sql,params):
        self.cursor.execute(sql,params)
    