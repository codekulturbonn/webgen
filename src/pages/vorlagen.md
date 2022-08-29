---
title: Technik & Vorlagen
summary: Du brauchst kein Techniker oder Künstler zu sein, um Dinge im Web zu veröffentlichen.
image:
    alt: Webgen
    src: ./images/huhn-1920.jpg
teaser_image:
    alt: webgen
    src: ./images/huhn-200.jpg
colors:
    background: blue
    accent: '#00c'
    footer:
        background: '#ccf'
        foreground: white
---
## Technik

das World-wide Web _WWW_, wie es von Sir Tim Berners-Lee Anfang der 1990er Jahre, also vor 30 Jahren, erfunden wurde, besteht aus ein paar Teilen:

### HTTP - das Hypertext-Transfer-Protokoll

Regeln, wie Seiten über das Internet übertragen werden. Diese Regeln sind im _HTTP-Protokoll_ zusammengefasst. HTTP steht für "Hypertext-Transfer-Protokoll".

Seiten werden per HTTP über eine Anfrage angefragt und in der antwort vom Server (das ist der gegenüberliegende Rechner) zurüchgeliefert.

Beispiel:

    telnet codekulturbonn.de 80

    GET /webgen/aaa.html HTTP/1.0

Diese Anfrage gibt den Inhalt der Seite zurück.

### URLs - Uniform Resource Locators

Seiten, Bilder und andere Dateien im Word-wide Web haben eine Adresse. Diese haben das Format

    https://codekulturbonn.de/webgen/aaa.html

Darin sind "https" das Schema, "codekulturbonn.de" der Rechnername, "/webgen/aaa.html" der Pfad zu der Datei auf diesem Rechner.

Es gibt noch zwei weitere Teile, die man seltener sieht:

    https://www.google.de/search?q=Clara-Schuhmann

Suchbegriffe können an Seiten hinter einem "?..." übergeben werden.

Stellen innerhalb einer Seite können durch Anhängen von "#..." angesprungen werden.

    https://codekulturbonn.de/webgen/bbb.html#abschnitt-2

### HTML - die Hypertext Markup Language

Eine Sprache für Seiten im WWW. Diese Sprache heißt _HTML_ ("Hypertext Markup Language") legt die Vokabeln (_Tags_, _Eigenschaften_) und Grammatik fest, in der Seiten geschrieben werden. 

Tags (groß oder klein geschrieben) werden in spitzen Klammern geschrieben und werden manchmal einzeln, manchmal paarweise verwandt:

    <p>Ich bin ein Absatz</p>
    
    <ul>
        <li>Eintrag eins</li>
        <li>Eintrag zwei</li>
    </u>

    <img src="../images/katze-80.jpg">

    <a href="./typen.html">Andere Seite</a>

Beispiele für Tags sind

* HTML - paarweise. Schließt die gesamte Seite ein. Eine HTML-Seite hat eine Kopf in HEAD und einen Rumpf in BODY, die als Paar jeweils weitere Tags einschliessen
* H1, H2, ... - paarweise. Überschriften auf verschiedenen Ebenen.
* P - paarweise. Absätze werden in P-Pärchen eingeschlossen. Absätze dürfen nicht geschachtelt werden.
* UL, OL - Listen mit Punkten oder Nummern. Listen können verschachtelt werden. Listeneinträge werden in Paare aus LI eingeschlossen.
* IMG - Bilder werden über IMG eingebunden. Die Bilddatei wird über ein _src_-Attribut benannt.
* A - Hyperlinks sind klickbare Textstellen, die zu anderen Seiten führen. Die Zielseite wird im _href_-Attribut benannt. Die drei Testseiten [Aaa](./aaa.html), [Bbb](./bbb.html), [Ccc](./ccc.html) sind untereinander verlinkt. 

## Vorlagen

In unseren ersten Webprojekten hatten wir [eine einfache Vorlage](https://github.com/,/webgen/blob/main/templates/article.mustache) selbst gebaut. Das ist nicht schwer. 

Hier ist eine vollständige Website:

    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>Eine einfache Webseite</title>
            <style>
            body { background-color: blue; }
            main {
                background-color: white;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
            }
            </style>
        </head>
        <body>
            <main>
                <h1>Willkommen auf meiner Website</h1>

                <p>Das hier ist nur ein Beispiel. Der Text steht auf 
                weißem Hintergrund, der Rand der Seite ist blau. 
                Texte bestehen aus</p> 
                
                <ul>
                    <li>Überschriften,</li>
                    <li>Absätzen,</li> 
                    <li>vielleicht auch noch Listen.</li>
                </ul>

                <p>Das Coolste an Websites sind Links. 
                Hier ist <a 
                    href="https://steinsekte.xyz">ein Link zur STEINsekte</a>.</p>
            </main>
        </body>
    </html>

Die Seite ist in HTML geschrieben und besteht aus dem Kopf in &lt;head> und dem Rumpf in &lt;body>. Im Rumpf stehen die Inhalte mit Texten, Bildern oder sogar Videos. 

Der Abschnitt in &lt;style> im Kopf ist ein Stylesheet in der Sprache CSS. Hiermit bestimmst du, wie die Seite und die Elemente darauf aussehen sollen. Also: Blauer Rahmen, Abstände, zentriert, diese und jene Schriftart.  

Um diese Seite im Browser (Firefox, Chrome) anzusehen, musst du den Text kopieren, als Datei mit der Endung `.html` speichern und im Browser öffnen. Hier ist die Seite im Editor. Auf meinem Mac benutze ich [Textmate](https://macromates.com/). Auf einem Linux-Rechner mit ElementaryOS kannst du den [Code-Editor](https://elementary.io/de/#showcase-code) benutzen. Wenn du auf Windows arbeiten musst, funktioniert [Notepad++](https://notepad-plus-plus.org/).

![Seite im Editor](images/SCR-20220829-qnb-200.png)

Hier ist die selbe Seite im Browser:

![Seite im  Browser](images/SCR-20220829-qtl-200.png)

Mit CMD-U auf dem Mac oder CTRL-U bzw. STRG-U kannst du dir übrigens immer den Quelltext der Seite ansehen.

Willst du mal etwas aufwändigere Designs ausprobieren, gibt es Seitenvorlagen zum Herunterladen. Hier sind ein paar Verzeichnisse:

* [W3Schools](https://www.w3schools.com/w3css/w3css_templates.asp)

Daneben gibt es auch Werkzeuge und spezielle Editoren zum Anlegen schicker Websites:

* [Website-Builder von NicePage](https://nicepage.com/html-website-builder) (Mac und Windows)
* [Blue Griffon](http://www.bluegriffon.org/)

Ich will nicht verschweigen, dass viele Leute Wordpress oder Tumblr benutzen. Das ist auch OK. irgendwie nicht OK ist, die eigenen, coolen Webprojekte auf den Seiten von Mark Zuckerberg, einem amerikanischen Milliardär, abzulegen. Zu seinen Seiten gehören Facebook, Instagram oder auch WhatApp. 