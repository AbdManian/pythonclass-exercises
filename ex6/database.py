import json

bank_accounts = {
    '1234-1363': dict(
        balance=2345,
        password='136363'
    ),

    '2345-1357': dict(
        balance=30000,
        password='5757'
    ),

    '3939-1381': dict(
        balance=700,
        password='8181'
    ),
}


def load_from_file(filename="db.json"):
    with open(filename, 'r') as f:
        bank_accounts.clear()
        bank_accounts.update(json.load(f))


def get_database():
    return bank_accounts
