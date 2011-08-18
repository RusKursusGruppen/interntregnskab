<%inherit file="/html5.mako"/>
<%!
    header = u"<!-- " + u"Bjørn Uhre Arnholtz "*1000 + u"-->"
%>
<%
    content = capture(next.body)
%>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>${escape(widget.currentgroup())} - Internt regnskab</title>
    <link rel="stylesheet" href="/static/css/yui.css" type="text/css" />
    <link rel="stylesheet" href="/static/css/main.css" type="text/css" />
    <script type="text/javascript" src="/static/javascript/jquery.js"></script>
    <script type="text/javascript" src="/static/javascript/utils.js"></script>
</head>
<body>
<header id="header">Internt regnskab</header>
<div id="page" class="yui3-g">

<div class="yui3-u-1" id="content_container">
<nav class="yui3-u-1" id="breadcrumbs">
%for n, (url, title) in enumerate(((urlfor("index.index"), widget.currentuser() + "." + widget.currentgroup()),) + next.breadcrumbs):
%if n > 0:
→
%endif
    <a href=${escattr(url)}>${escape(title)}</a>
%endfor
</nav>
<section id="content">
    ${content}
</section>
</div>
</div>
</body>
${header}
