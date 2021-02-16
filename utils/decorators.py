
def verify_auth(operation):
    def wrapper(*args, **kwargs):
        if args[0].is_auth:
            return operation(*args, **kwargs)
        else:
            print("Please, to do this operation you need to authenticate first!")
    return wrapper
