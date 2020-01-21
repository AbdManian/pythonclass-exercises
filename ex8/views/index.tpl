<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <link rel="stylesheet" href="/static/css/metro-all.min.css">
  </head>
  <body>

        <div class="img-container">
            <img src="/static/img/kcb.svg" style="width:60%">
        </div>

      <script src="/static/js/metro.min.js"></script>
      <div class="container">
        <!-- <h1 class="text-center"> KC Bank </h1> -->
        <p>
        <p>

        <h2> Customer Operations </h2>
        <form action="/customer/getotp">
            <button class="button success" type="submit">Get Dynamic Password</button>
        </form>
          <!--
        <p>
        <form action="/customer/transfer">
            <button class="button success" type="submit">Money Transfer</button>
        </form>
-->
        <h2> Bank Operations </h2>
        <form action="/bank/view">
            <button class="button success" type="submit">View Accounts</button>
        </form>
          <p>
        <form action="/bank/addaccount">
            <button class="button success" type="submit">Add New Account</button>
        </form>
      </div>
  </body>
</html>