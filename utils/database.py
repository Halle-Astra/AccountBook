import os

data_root = 'database'

def isNeedRegister(register_name):
    users_list = os.listdir(data_root)
    if register_name in users_list:
        return False
    else:
        return True


def registerAccount(register_name):
    account_file = os.path.join(data_root, register_name)
    if not os.path.exists(account_file):
        f = open(account_file,"w")
        f.close()