<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <link rel="stylesheet" href="/static/css/metro-all.min.css">
  </head>
  <body>

    <div class="container">
        <h1>Add New Costumer Account</h1>
        <form action="/bank/addaccount" method="post">
            <p>Name</p>
            <input name="name" type="text" data-role="input">
            <p>Account Number</p>
            <input name="account" type="text" data-role="input">
            <p>Deposit Amount</p>
            <input name="money" type="text" data-role="input">
            <p>Access Password</p>
            <input name="password" type="password" data-role="input">
            <small class="text-muted">Account Static Access Password</small>
            <p></p>
            <button class="button success" type="submit">Add New Account</button>

        </form>

    </div>



      <script src="/static/js/metro.min.js"></script>
  </body>
</html>

