from database.sql import QueryExecutor, QueryGenerator


class DBManager:
    def __init__(self, db_path):
        self.query_exec = QueryExecutor(db_path)
        self.query_gen = QueryGenerator()
        self.__setup()

    def __setup(self):
        self.query_exec.create_table(self.query_gen.create_user_tbl())
        self.query_exec.create_table(self.query_gen.create_user_info_tbl())
        self.query_exec.create_table(self.query_gen.create_password_tbl())

    def add_new_user(self, user, passwd):
        query, param = self.query_gen.add_new_user(user, passwd)
        self.query_exec.modify_data(query, param)

    def add_user_info(self, user, email):
        query, param = self.query_gen.add_user_info(user, email)
        self.query_exec.modify_data(query, param)

    def add_password(self, account, user, passwd, sitename="", website=""):
        query, param = self.query_gen.add_password(
            account, user, passwd, sitename, website
        )
        self.query_exec.modify_data(query, param)

    def delete_password(self, account, user, passwd, site):
        query, param = self.query_gen.delete_password(account, user, passwd, site)
        self.query_exec.modify_data(query, param)

    def get_user_email(self, user):
        query, param = self.query_gen.user_email(user)
        email = self.query_exec.get_user_email(query, param)
        return email

    def get_all_passwords_for_a_user(self, user) -> list:
        """Gets all the passwords created by a single account."""
        query, params = self.query_gen.get_account_passwords(user)
        data = self.query_exec.account_passwords(query, params)
        return data

    def is_valid_user(self, user, password) -> int:
        """Checks if the user and it's credentials are correct.

        Returns
        -------
        :int
            integer number corresponding to the status of auth
            1 => credentials are valid
            2 => user does not exist
            3 => password is incorrect
        """
        query, param = self.query_gen.user_auth(user)
        validity_status = self.query_exec.authenticate_user(query, param, password)
        return validity_status
