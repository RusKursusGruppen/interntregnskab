<%inherit file="/main.mako"/>
<%!
    from app.utils.currency import formatcurrency
    import app.utils.date as dateutils
%>
<%
    self.breadcrumbs = ()
    accounts = [[u"Bjørn", 400000]]
%>
<h1>Velkommen til internt regnskab</h1>

<h3>Status</h3>
<table>
    <thead>
        <tr>
            <th>Navn</th>
            <th>Saldo</th>
        </tr>
    </thead>
    <tbody>
%for name, balance in accounts:
        <tr>
            <td>${escape(name)}</td>
            <td>${formatcurrency(balance)}</td>
        </tr>
%endfor
    </tbody>
</table>


<%
    entries = [
        [
            dateutils.now(), "bjorn", u"Øl "*16, u"bjorn", 400000, [
                [u"Bjørn", 3223, 4],
                [u"Lund",  2332, 1],
                [u"Jenny", 2332, 3]
            ]
        ]
    ]
%>
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
        </tr>
    </thead>
    <tbody>
%for date, username, description, creditor, amount, debtors in entries:
<%
    delta = date - dateutils.now()
%>
        <tr>
            <td>${dateutils.formatdelta(delta)}</td>
            <td>${escape(username)}</td>
            <td>${escape(description)}</td>
            <td>${escape(creditor)}</td>
            <td>${formatcurrency(amount)}</td>
            <td>
%for n, (name, amount, weight) in enumerate(debtors):
%if n != 0:
                <br/>
%endif
                ${escape(name)}: ${weight} (${formatcurrency(amount)})
%endfor
            </td>
        </tr>
%endfor
    </tbody>
</table>
