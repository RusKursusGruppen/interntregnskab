<%inherit file="/main.mako" />
<%
    self.breadcrumbs = (
        (urlfor("login.chpasswd_form"), u"Skift løsen"),
    )
%>
<h1>Skift løsen</h1>
%if first_time:
<p>
    <strong>Vigtigt</strong>:
    Da dit nuværende løsen er ment som et midlertidigt
    løsen, bedes du venligst ændre dit løsen til et andet.
</p>
%endif
%if error_length:
<p style="color:red">
    Du har glemt at udfylde et af felterne.
</p>
%endif
%if error_match:
<p style="color:red">
    De to indtastede løsener var ikke ens.
</p>
%endif
<form method="post" action=${escattr(urlfor("login.chpasswd_do"))}>
<table>
    <tr>
        <td><label for="password0">Ny løsen:</td>
        <td><input type="password" name="password0" id="password0"/></td>
    </tr>
    <tr>
        <td><label for="password1">Gentag nyt løsen:</td>
        <td><input type="password" name="password1" id="password1"/></td>
    </tr>
    <tr>
        <td colspan="2" style="text-align:right;">
            <input type="submit" value="Skift løsen"/>
        </td>
    </tr>
</table>
</form>
