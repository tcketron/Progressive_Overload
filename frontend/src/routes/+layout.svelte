<header>
    <h1>Progressive Overload</h1>
    <nav>
        <ul id="menu">
            <li><a href="/data/legs">Legs</a></li>
            <li><a href="/data/push">Push</a></li>
            <li><a href="/data/pull">Pull</a></li>
            <li><a href="/">Home</a></li>
        </ul>
    </nav>
</header>
<body>
</body>

<slot />

<style>
    ul#menu li {
      display:inline;
      align-items:right;
      justify-content:right;
      list-style:none;
    }

    header{
        background-color: rgb(40, 44, 52);
        height: 80px;
        width: 100%;
        margin: 0;
        margin-left: 0;
        padding: 0px;
        position: absolute;
        top: 0;
    }

    li a {
        float:right;
        display: inline;
        color: rgb(220, 223, 228);
        line-height: 50px;
        padding-left: 20px;
        padding-right: 20px;
        text-decoration: none;
        margin: 0;
        height: 100%;
    }

    li a:hover {
        color: rgb(244, 244, 244);
    }

    body {
        margin: 0;
        padding: 0;
        padding-top: 30px;
    }

    h1 {
        margin: 0;
        padding: 0;
        padding-top:20px;
        float:left;
        color: rgb(220, 223, 228);
    }

    body {
        background-color: rgb(28, 31, 36);
    }

</style>
<!-- 
Style colors:
Black - 40, 44, 52 (bright black - 90, 99, 116)
Red - 224, 108, 117
Green - 152, 195, 121
Yellow - 229, 192, 123
Blue - 97, 175, 239
Purple - 198, 120, 221
Cyan - 86, 182, 194
White - 220, 223, 228
Background - 28, 31, 36
 -->