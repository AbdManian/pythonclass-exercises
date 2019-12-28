<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <link rel="stylesheet" href="/static/css/metro-all.min.css">
  </head>
  <body>

    <div class="container"  style="width:60%">
        <h2>Accounts List</h2>
        <table class="table striped">
            <thead>
            <tr>
                <th>#</th>
                <th>Account</th>
                <th>Balance</th>
            </tr>
            </thead>

            <tbody>
            %for i, info in enumerate(accounts):
            <tr>
                <td>{{i+1}}</td>
                <td><a href="/bank/view/{{info['account']}}">{{info['account']}}</td>
                <td>{{info['balance']}}</td>
            </tr>
            %end
            </tbody>
        </table>

    </div>



      <script src="/static/js/metro.min.js"></script>
  </body>
</html>

