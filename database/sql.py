from inspect import Parameter
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
        params = (username, password)
        return (query, params)

    def add_user_info(self, username, email) -> tuple:
        query = f"""INSERT INTO {self.__account_info_table} (USERNAME, EMAIL) VALUES (?, ?)"""
        params = (username, email)
        return (query, params)

    def add_password(self, username, password, sitename="", website_url="") -> tuple:
        current_datetime = str(datetime.datetime.now())
        query = f"""INSERT INTO {self.__password_table} 
            (USERNAME, SITENAME, WEBSITE_URL, PASSWORD, CREATION_TIME, LAST_MODIFY_TIME) 
            VALUES (?, ?, ?, ?, ?, ?);"""
        params = (username, sitename, website_url, 
            password, current_datetime, current_datetime)
        return (query, params)

    def delete_password(self, username, password, sitename, website_url) -> tuple:
        query = f"""DELETE FROM {self.__password_table} 
            WHERE USERNAME=:username 
            AND PASSWORD=:password
            AND SITENAME=:sitename
            AND WEBSITE_URL=:website_url;"""
        params = {
            "username":username,
            "password":password,
            "sitename":sitename,
            "website_url":website_url
        }
        return (query, params)

    def user_auth(self, username) -> tuple: 
        query = f"""SELECT PASSWORD FROM {self.__account_table} WHERE USERNAME=:username;"""
        params = {"username":username}
        return (query, params)

    def user_email(self, username) -> tuple:
        query = f"""SELECT EMAIL from {self.__account_info_table} WHERE USERNAME=:username;"""
        params = {"username":username}
        return (query, params)


class QueryExecutor:
    def __init__(self, sqlite_file_path:str, log=1):
        self.conn = sqlite3.connect(sqlite_file_path)
        self.cursor = self.conn.cursor()
        self.log = log
        if self.log: print(f"[+] Connect to database at {sqlite_file_path}")

    def create_table(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def modify_data(self, query, params):
        self.cursor.execute(query, params)
        self.conn.commit()

    def authenticate_user(self, query, params, password) -> bool:
        self.cursor.execute(query, params)
        fetched_password = self.cursor.fetchone()
        if (fetched_password[0] == password):
            if self.log: print(f"[+] Sucessfully authenticated {params['username']}")
            return True
        return False

    def get_user_email(self, query, params) -> str:
        self.cursor.execute(query, params)
        fetched_email = self.cursor.fetchone()
        if fetched_email == None:
            if self.log: print(f"[!] User {params['username']} not found")
            return ""
        return fetched_email[0]