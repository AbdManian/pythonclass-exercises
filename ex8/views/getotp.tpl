<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <link rel="stylesheet" href="/static/css/metro-all.min.css">
  </head>
  <body>

    <div class="container">
        <h1>Get One Time Password</h1>
        <form action="/customer/getotp" method="post">
            <p>Account Number</p>
            <input name="account" type="text" data-role="input">
            <p>Password</p>
            <input name="password" type="password" data-role="input">
            <small class="text-muted">Enter account's static password</small>
            <p></p>


            <button class="button success" type="submit">Get One-Time Password</button>

        </form>

    </div>



      <script src="/static/js/metro.min.js"></script>
  </body>
</html>

