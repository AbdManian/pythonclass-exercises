<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <link rel="stylesheet" href="/static/css/metro-all.min.css">
  </head>
  <body>

    <div class="container">
        <h1>Wire Transfer</h1>
        <form action="/customer/transfer" method="post">
            <p>Origin Account</p>
            <input name="origin" type="text" data-role="input">

            <p>Password</p>
            <input name="password" type="password" data-role="input">
            <small class="text-muted">Enter dynamic one-time password</small>

            <p>Transfer to</p>
            <input name="destination" type="text" data-role="input">

            <p>Amount</p>
            <input name="amount" type="text" data-role="input">

            <p></p>


            <button class="button success" type="submit">Transfer</button>

        </form>

    </div>



      <script src="/static/js/metro.min.js"></script>
  </body>
</html>

