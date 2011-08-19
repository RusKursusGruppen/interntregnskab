<%inherit file="/main.mako" />
<%
    self.breadcrumbs = (
        (urlfor("entries.new_form"), "Ny indtastning"),
    )
%>
<h1>Ny indtastning</h1>
<form method="post" action=${escattr(urlfor("entries.new_do"))}>
<table>
<tbody>
    <tr>
        <td><label for="creditor">Ulækker</label></td>
        <td>
            <select name="creditor" id="creditor">
%for uid, name in members:
%if name == widget.currentuser():
                <option value=${escattr(uid)} selected="selected">${escape(name)}</option>
%else:
                <option value=${escattr(uid)}>${escape(name)}</option>
%endif
%endfor
            </select>
        </td>
    </tr>
    <tr>
        <td><label for="description">Beskrivelse</label></td>
        <td><input type="text" id="description" name="description"/></td>
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
%for uid, name in members:
<% nameattr = escattr("member_" + uid) %>
        <tr>
            <td><label for=${nameattr}>${escape(name)}</label></td>
            <td><input type="text" name=${nameattr} id=${nameattr} value="0"/></td>
        </tr>
%endfor
    </tbody>
</table>

<input type="submit" value="Før ind i regnskabet" />
</form>
