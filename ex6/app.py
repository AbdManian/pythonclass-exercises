from bottle import route, static_file, template, run, post, request

import logic

@route('/favicon.ico')
def server_favicon():
    print("Here for FAV")
    return static_file('/favicon.ico', root='./static/img')

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


@route('/customer/getotp')
def get_otp():
    return template('getotp', data={})


@post('/customer/getotp')
def get_otp():
    account = request.forms.get('account')
    password = request.forms.get('password')
    return logic.get_one_time_password(account, password)


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
    return template('accountlist', accounts=logic.get_account_list())


@route('/bank/view/<account_id>')
def view_account(account_id):
    info = logic.get_account_info(account_id)
    return template('accountinfo', info=info)


# Root
@route('/')
def index():
    data = {}
    return template('index', data=data)


run(host='localhost', port=8080, debug=True, reloader=True)
