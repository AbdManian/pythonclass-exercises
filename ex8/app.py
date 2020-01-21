from bottle import route, static_file, template, run, post, request

import logic
import database

@route('/favicon.ico')
def server_favicon():
    return static_file('/favicon.ico', root='./static/img')

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


@route('/customer/getotp')
def get_otp():
    return template('getotp', data={})


@post('/customer/getotp')
def get_otp():
    account_id = request.forms.get('account')
    password = request.forms.get('password')

    account = database.get_account_by_id(account_id)
    if account is None:
        return "Account not found!"

    if not hasattr(account, 'get_otp'):
        return '"get_otp()" is not defined in class'

    ret = account.get_otp(password)

    return database.update_account(account) + " " + ret


@route('/customer/transfer')
def transfer():
    return template('transfer', data={})


@post('/customer/transfer')
def transfer():
    tr_data = dict(
        origin=request.forms.get('origin'),
        password=request.forms.get('password'),
        destination=request.forms.get('destination'),
        amount=request.forms.get('amount')
    )
    return logic.do_transfer(tr_data)


@route('/bank/view')
def view_accounts():
    accounts = database.get_account_list()
    return template('accountlist', accounts=accounts)


@route('/bank/view/<account_id>')
def view_account(account_id):
    return database.get_info_by_account_id(account_id)


@route('/bank/addaccount')
def view_accounts():
    return template('addaccount', data={})


@post('/bank/addaccount')
def get_otp():
    account_info = dict(
        name=request.forms.get('name'),
        account=request.forms.get('account'),
        money=request.forms.get('money'),
        password=request.forms.get('password'),
    )

    new_account = logic.create_new_account(account_info)

    return database.add_new_account(new_account)



# Root
@route('/')
def index():
    data = {}
    return template('index', data=data)


database.setup()

run(host='localhost', port=8080, debug=True, reloader=True)
