from pynubank import Nubank
from utils.decorators import verify_auth, verify_credit_data, verify_account_data
import pandas as pd
import os

class Bank:
    def __init__(self, user_id):
        self.__api = Nubank()
        self.__is_auth = False
        self.__user_id = user_id
        self.__credit_data_path = f"{os.getcwd()}/data/{self.__user_id}/credit_history.csv"
        self.__account_data_path = f"{os.getcwd()}/data/{self.__user_id}/account_history.csv"
        self.__funds = {
            "credit": self.__credit_data_path,
            "account": self.__account_data_path
        }

    @property
    def user_id(self):
        return self.__user_id

    @property
    def is_auth(self):
        return self.__is_auth

    def auth(self, user_cpf:str, user_password:str, cert_path:str):
        """
        :param user_cpf: user's cpf
        :type str
        :param user_password: user's password
        :type str
        :param cert_path: certification's path
        :type str
        """
        try:
            self.__api.authenticate_with_cert(user_cpf, user_password, cert_path)
            self.__is_auth = True
        except Exception as e:
            print(e)

    def __limit_history(self, history, limit:int):
        return history.sample(limit) if limit else history

    @verify_auth
    def __get_api_data(self, fund):
        funds = {
            'credit': self.__api.get_card_statements,
            'account': self.__api.get_account_statements
        }
        method = funds[fund]
        return method()

    def fetch_data(self, fund):
        try:
            df = pd.DataFrame(
                self.__get_api_data(fund)
            )
            df.to_csv(self.__funds[fund], index=False)
            print(f'Success fetching data from {fund}')
        except Exception as e:
            print(e)

    @verify_credit_data
    def credit_history(self, limit:int=None):
        """
        :param limit: credit card history statements rows limit
        :type int
        """
        df = pd.read_csv(
            self.__credit_data_path
        )            
        return self.__limit_history(
            df,
            limit
        )

    @verify_account_data
    def account_history(self, limit:int=None):
        """
        :param limit: account history statements rows limit
        :type int
        """
        df = pd.read_csv(
            self.__account_data_path
        )
        return self.__limit_history(
            df,
            limit
        )

    def check_local_data(self, fund):
        return os.access(self.__funds[fund], os.F_OK)
