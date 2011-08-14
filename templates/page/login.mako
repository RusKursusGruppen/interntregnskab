<%inherit file="/html5.mako" />
<head>
    <title>Internt Regnskab - Login</title>
    <link rel="stylesheet" href="/static/css/main.css" type="text/css" />
    <link rel="icon" href="/static/beer.ico" type="image/x-icon" />
    <script type="text/javascript" src="/static/javascript/jquery.js"></script>
</head>
<body id="enter_title">
<form action=${escattr(urlfor("login.authenticate"))} method="post" id="enter_title_form">
    <h1>Login</h1>
    <p>
        Velkommen til <strong>internt regnskab</strong>. Log ind
        med dit RKG brugernavn og løsen.
    </p>
    <table>
%if error_length:
        <tr>
            <td colspan="2" style="color:red;">
                Enten dit brugernavn eller adgangskode er ikke
                udfyldt.
            </td>
        </tr>
%endif
%if error_invalid:
        <tr>
            <td colspan="2" style="color:red;">
                Ugyldig brugernavn eller adgangskode.
            </td>
        </tr>
%endif
        <tr>
            <td><label for="username">Brugernavn</label></td>
            <td>
                <input type="text" name="username" id="username" />
            </td>
        </tr>
        <tr>
            <td><label for="password">Adgangskode</label></td>
            <td>
                <input type="password" name="password" id="password" />
            </td>
        </tr>
        <tr>
            <td colspan="2" style="text-align:right;">
                <input type="submit" value="Login" />
            </td>
        </tr>
    </table>
</form>
</body>
