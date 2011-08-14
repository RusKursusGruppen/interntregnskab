<%inherit file="/main.mako"/>
<%
    from pprint import pformat
    self.breadcrumbs = ()
%>
<h1>Test side</h1>
<pre>
    ${escape(pformat(test))}
</pre>
