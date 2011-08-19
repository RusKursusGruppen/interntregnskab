<%inherit file="/main.mako"/>
<%!
    from app.utils.currency import formatcurrency
    import app.utils.date as dateutils
%>
<%
    self.breadcrumbs = ()
%>
<h1>Velkommen til internt regnskab</h1>
<h3>Status</h3>
<p>
    <a href=${escattr(urlfor("login.chpasswd_form"))}>Klik her for at skifte dit løsen</a>
</p>
<table>
    <thead>
        <tr>
            <th>Navn</th>
            <th>Saldo</th>
        </tr>
    </thead>
    <tbody>
%for name, balance in balances:
        <tr>
            <td>${escape(name)}</td>
            <td>${formatcurrency(balance)}</td>
        </tr>
%endfor
    </tbody>
</table>

<h3>Registreringer</h3>
<p>
    <a href=${escattr(urlfor("entries.new_form"))}>Indtast ny registrering</a>
</p>
<table id="entriestable">
    <thead>
        <tr>
            <th>Dato</th>
            <th>Brugernavn</th>
            <th>Beskrivelse</th>
            <th>Ulækker</th>
            <th>Beløb</th>
            <th>Skyldnere</th>
            <th>Slet</th>
        </tr>
    </thead>
    <tbody>
%for entry in entries:
%if entry["deletedby"] is None:
        <tr>
%else:
        <tr style="color:gray;">
%endif
            <td>${widget.timedelta(entry["date"])}</td>
            <td>${escape(entry["username"])}</td>
            <td>${escape(entry["description"])}</td>
            <td>${escape(entry["creditor"])}</td>
            <td>${formatcurrency(entry["amount"])}</td>
            <td>
%for n, (debtor,weight) in enumerate(entry["debtors"].items()):
%if n != 0:
                <br/>
%endif
                ${escape(debtor)}: ${weight}
%endfor
            </td>
            <td>
%if entry["deletedby"] is None:
    <a href=${escattr(urlfor("entries.delete", id=entry["id"]))}>[Slet]</a>
%else:
    Slettet af ${escape(entry["deletedby"])}
%endif
            </td>
        </tr>
%endfor
    </tbody>
</table>
