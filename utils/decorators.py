
def verify_auth(operation):
    def wrapper(*args, **kwargs):
        bank = args[0]
        if bank.is_auth:
            return operation(*args, **kwargs)
        else:
            raise Exception("Please, to do this operation you need to authenticate first!")
    return wrapper

def verify_account_data(operation):
    def wrapper(*args, **kwargs):
        bank = args[0]
        if not bank.check_local_data('account'):
            bank.fetch_data('account')
        return operation(*args, **kwargs)
    return wrapper

def verify_credit_data(operation):
    def wrapper(*args, **kwargs):
        bank = args[0]
        if not bank.check_local_data('credit'):
            bank.fetch_data('credit')
        return operation(*args, **kwargs)

    return wrapper
