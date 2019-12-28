import database


#database.load_from_file()

def get_one_time_password(account, static_password):
    return 'Not implemented account="{}" pass="{}"'.format(account, static_password)


def do_transfer(transfer_info):
    return 'Not implemented transfer_info={}'.format(str(transfer_info))


def get_account_list():
    acc_list = [
        dict(account='NotImplemented_1', balance='xxxx'),
        dict(account='NotImplemented_2', balance='yyyy'),
        dict(account='NotImplemented_3', balance='zzzz'),
    ]

    return acc_list


def get_account_info(account):
    info = dict(
        account=account,
        balance='xyz',
        static_pass='NOT IMPLEMENTED',
        dynamic_pass_expire='Expired|X sec',

    )

    return info


