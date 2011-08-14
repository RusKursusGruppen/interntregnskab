<%inherit file="/html5.mako"/>
<%!
    header = u"<!-- " + u"Bjørn Uhre Arnholtz "*1000 + u"-->"
    navbar_links = (
        ("index.index", u"Status", "home"),
    )
%>
<%
    content = capture(next.body)
%>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Internt regnskab</title>
    <link rel="stylesheet" href="/static/css/yui.css" type="text/css" />
    <link rel="stylesheet" href="/static/css/main.css" type="text/css" />
    <link rel="icon" href="/static/beer.ico" type="image/x-icon" />
    <script type="text/javascript" src="/static/javascript/jquery.js"></script>
    <script type="text/javascript" src="/static/javascript/utils.js"></script>
</head>
<body>
<header id="header">Internt regnskab</header>
<div id="page" class="yui3-g">

<nav class="yui3-u-1-5" id="nav_container">
    <ul id="nav">
%for target, text, id in navbar_links:
        <li id=${escattr("nav_"+id)}><a href=${escattr(urlfor(target))}>${escape(text)}</a></li>
%endfor
    </ul>
</nav>

<div class="yui3-u-4-5" id="content_container">
<nav class="yui3-u-1" id="breadcrumbs">
%for n, (url, title) in enumerate(((urlfor("index.index"), u"Status"),) + next.breadcrumbs):
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
