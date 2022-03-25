import os
import datetime
import sqlite3

class QueryGenerator:
    """Main work is to generate queries to be used by the controller."""
    def __init__(self):
        self.__account_table = "User"
        self.__account_info_table = "User_Info"
        self.__password_table = "Password"

    # setters
    def set_account_table_name(self, new_name:str): 
        self.__account_table = new_name

    def set_user_info_table_name(self, new_name:str): 
        self.__account_info_table = new_name

    def set_password_table_name(self, new_name:str): 
        self.__password_table = new_name

    # getters
    def get_account_table_name(self) -> str: 
       return self.__account_table

    def get_user_info_table_name(self) -> str: 
        return self.__account_info_table

    def get_password_table_name(self) -> str: 
        return self.__password_table

    def create_user_tbl(self):
        return f"""CREATE TABLE IF NOT EXISTS {self.__account_table}
            (
                USERNAME TEXT NOT NULL,
                PASSWORD TEXT NOT NULL
            );
            """

    def create_user_info_tbl(self):
        return f"""CREATE TABLE IF NOT EXISTS {self.__account_info_table}
            (
                USERNAME TEXT NOT NULL,
                EMAIL TEXT NOT NULL
            );
            """

    def create_password_tbl(self):
        return f"""CREATE TABLE IF NOT EXISTS {self.__password_table}
            (
                USERNAME TEXT NOT NULL,
                SITENAME TEXT,
                WEBSITE_URL TEXT,
                PASSWORD TEXT NOT NULL,
                CREATION_TIME TEXT NOT NULL,
                LAST_MODIFY_TIME TEXT NOT NULL
            );
            """
    def add_new_user(self, username, password) -> tuple:
        query = f"""INSERT INTO {self.__account_table} (USERNAME, PASSWORD) VALUES (?, ?)"""
        parameters = (username, password)
        return (query, parameters)

    def add_user_info(self, username, email) -> tuple:
        query = f"""INSERT INTO {self.__account_info_table} (USERNAME, EMAIL) VALUES (?, ?)"""
        parameters = (username, email)
        return (query, parameters)

    def add_password(self, username, password, sitename="", website_url="") -> tuple:
        current_datetime = str(datetime.datetime.now())
        query = f"""INSERT INTO {self.__password_table} 
            (USERNAME, SITENAME, WEBSITE_URL, PASSWORD, CREATION_TIME, LAST_MODIFY_TIME) 
            VALUES (?, ?, ?, ?, ?, ?);"""
        parameters = (username, sitename, website_url, 
            password, current_datetime, current_datetime)
        return (query, parameters)


class QueryExecutor:
    def __init__(self, sqlite_file_path:str, log=1):
        self.conn = sqlite3.connect(sqlite_file_path)
        self.cursor = self.conn.cursor()
        if log: print(f"[+] Connect to database at {sqlite_file_path}")

    def create_table(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, query, parameters):
        self.cursor.execute(query, parameters)
        self.conn.commit()