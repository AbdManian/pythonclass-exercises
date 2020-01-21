import json
import account
import pickle
import collections

_db = {}

def add_new_account(new_account):
    if new_account.__class__.__name__ != 'Account':
        return "Account instance is required. Get " + str(new_account)

    if not hasattr(new_account, 'account'):
        return '<b>account</b> is not defined in the object!'

    _db[new_account.account] = new_account

    save_database(_db)

    return "New account is added to the database"


def update_account(account):
    if account.__class__.__name__ != 'Account':
        return "Account instance for update required"

    if not hasattr(account, 'account'):
        return '<b>account</b> is not defined in the object!'

    if account.account not in _db:
        return "Account not founded in database!"

    _db[account.account] = account

    save_database(_db)

    return ""

def get_account_list():
    return [_create_db_entry_to_table_row(x) for x in _db.values()]



def get_account_by_id(account_id):
    return _db.get(account_id, None)


def get_info_by_account_id(account_id):
    if account_id not in _db:
        return "<b>{}</b> not found!".format(account_id)

    account = _db[account_id]

    get_info = getattr(account, 'get_info', None)
    if callable(get_info):
        account_info = get_info()
    else:
        account_info = '"get_info()" is not defined in class'

    return account_info


def _create_db_entry_to_table_row(db_entry):
    if db_entry.__class__.__name__ != 'Account':
        return collections.defaultdict(lambda:"Not a Account Instance!")

    otp_state_func = getattr(db_entry, 'get_otp_state', None)
    if callable(otp_state_func):
        otp_state = otp_state_func()
    else:
        otp_state = '"get_otp_state()" is not defined in class'

    ret = dict(
        name=getattr(db_entry, 'name', 'name not defined'),
        account=getattr(db_entry, 'account', 'account not defined'),
        balance=getattr(db_entry, 'money', 'money not defined'),
        otp_state=otp_state,
    )
    return ret


def save_database(data_base):
    try:
        with open('db.bin', 'wb') as f:
            pickle.dump(data_base, f)
    except:
        print("Error in saving database = ", str(data_base))

def setup():
    # Check for database
    global _db
    try:
        with open('db.bin', 'rb') as f:
            _db = pickle.load(f)
    except:
        print("Error in accessing database file!")

    save_database(_db)
