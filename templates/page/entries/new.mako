<%inherit file="/main.mako" />
<%
    self.breadcrumbs = (
        (urlfor("entries.new_form"), "Ny indtastning"),
    )
    members = ("bjorn", "lund", "jenny", "emil", "sorend")
%>
<h1>Ny indtastning</h1>
<form method="post" action=${escattr(urlfor("entries.new_do"))}>
<table>
<tbody>
    <tr>
        <td><label for="creditor">Ulækker</label></td>
        <td>
            <select name="creditor" id="creditor">
%for name in members:
                <option value=${escattr(name)}>${escape(name)}</option>
%endfor
            </select>
        </td>
    </tr>
    <tr>
        <td><label for="amount">Beløb</label></td>
        <td><input type="text" id="amount" name="amount"/></td>
    </tr>
</tbody>
</table>

<table>
    <thead>
        <tr>
            <th>Navn</th>
            <th>Vægtet fordeling</th>
        </tr>
    </thead>
    <tbody>
%for name in members:
<% nameattr = escattr("member_" + name) %>
        <tr>
            <td><label for=${nameattr}>${escape(name)}</label></td>
            <td><input type="text" name=${nameattr} id=${nameattr} value="0"/></td>
        </tr>
%endfor
    </tbody>
</table>

<input type="submit" value="Før ind i regnskabet" />
</form>
