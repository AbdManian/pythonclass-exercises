<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <link rel="stylesheet" href="/static/css/metro-all.min.css">
  </head>
  <body>

    <div class="container"  style="width:80%">
        <h2>Account Info ({{info['account']}})</h2>
        <p></p>
        <p><strong>Account: </strong>{{info['account']}}</p>
        <p><strong>Balance: </strong>{{info['balance']}}</p>
        <p><strong>Static Pass: </strong>{{info['static_pass']}}</p>
        <p><strong>OTP TTL: </strong>{{info['dynamic_pass_expire']}}</p>



    </div>



      <script src="/static/js/metro.min.js"></script>
  </body>
</html>

