from pynubank import Nubank
from utils.decorators import verify_auth
import pandas as pd
import os

class Bank:
    def __init__(self):
        self.__api = Nubank()
        self.__is_auth = False
        self.__credit_data_path = f"{os.getcwd()}/data/credit_history.csv"
        self.__account_data_path = f"{os.getcwd()}/data/account_history.csv"
    
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

    def credit_history(self, limit:int=None):
        """
        :param limit: credit card history statements rows limit
        :type int
        """
        fund = 'credit'
        if self.check_local_data(fund):
            df = pd.read_csv(
                self.__credit_data_path
            )
        else:
            df = pd.DataFrame(
                self.__get_api_data(fund)
            )
            df.to_csv(self.__credit_data_path, index=False)
        return self.__limit_history(
            df,
            limit
        )

    def account_history(self, limit:int=None):
        """
        :param limit: account history statements rows limit
        :type int
        """
        fund = 'account'
        if self.check_local_data(fund):
            df = pd.read_csv(
                self.__account_data_path
            )
        else:
            df = pd.DataFrame(
                self.__get_api_data(fund)
            )
            df.to_csv(self.__account_data_path, index=False)
        return self.__limit_history(
            df,
            limit
        )

    def check_local_data(self, fund):
        funds = {
            "credit": self.__credit_data_path,
            "account": self.__account_data_path
        }
        return os.access(funds[fund], os.F_OK)
