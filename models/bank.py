from pynubank import Nubank
from utils.decorators import verify_auth
import pandas as pd


class Bank:
    def __init__(self):
        self.__api = Nubank()
        self.__is_auth = False
    
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

    def __get_history(self, method, limit:int):
        all_history = pd.DataFrame(
            method()
        )
        return all_history.sample(limit) if limit else all_history

    @verify_auth
    def credit_history(self, limit:int=None):
        """
        :param limit: credit card history statements rows limit
        :type int
        """
        return self.__get_history(
            self.__api.get_card_statements,
            limit
        )

    @verify_auth
    def account_history(self, limit:int=None):
        """
        :param limit: account history statements rows limit
        :type int
        """
        return self.__get_history(
            self.__api.get_account_statements,
            limit
        )
