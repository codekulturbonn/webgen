---
title: Webgen
summary: Ein einfacher Seitengenerator in Python.
image:
    alt: Webgen
    src: ./images/katze-1920.jpg
teaser_image:
    alt: webgen
    src: ./images/katze-200.jpg
colors:
    background: red
    accent: '#c00'
    footer:
        background: '#fcc'
        foreground: white
---
Webseiten kannst du in HTML (_Hypertext Markup Language_) einfach mit der Hand schreiben. Ein paar Dinge lassen sich aber automatisieren. Dabei hilft dieses kleine Python-Programm. Es erzeugt (_generiert_) HTML-Seiten aus Inhalten, Vorlagen (_Templates_), Bildern und Stilvorlagen (_Style Sheets_ in der Sprache _CSS_ - Cascading Style Sheets).

Der Generator verwendet einige Bibliotheken, um seine Aufgaben zu erledigen:

* Einstellungen im YAML-Format: [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation)
* Seitenvorlagen im Mustache-Format: [Chevron](https://github.com/noahmorrison/chevron)
* Seiten mit [Markdown](https://github.com/Python-Markdown/markdown)
  ... und Frontmatter: [Python Frontmatter](https://python-frontmatter.readthedocs.io/) 
* Bilder verkleinern mit [Pillow](https://pillow.readthedocs.io/) 

## Alternativen

Ehrlich gesagt, ich würde diesen Generator nicht für größere Projekte verwenden. Er tut allerdings alles, was wir für unsere Experimente mit Webseiten brauchen. Besonders Bilder verkleinern andere, ähnliche Programme nicht. Und auch keine Adventskalender erzeugen.

Hier sind ein paar Alternativen:

* [Ivy](http://www.dmulholl.com/docs/ivy/dev/index.html) von Darren Mulholland. Ich mag die Einfachheit und Erweiterbarkeit. [Code. Kultur. Bonn](https://codekulturbonn.de/) und [mein Weblog](https://olav.net) sind damit gebaut.
* [Awesome Static Site Generators](https://github.com/myles/awesome-static-generators). Eine Riesenliste mit ähnlichen Werkzeugen. 

### Gemini

Wenn selbst eine Website zu aufwängig scheint: Vielleicht reicht auch eine Gemini-Seite. [Das Format](https://gemini.circumlunar.space/docs/specification.gmi) ist viel einfacher als HTML. Hier kannst du Gemini-Seiten veröffentlichen:

* https://gemlog.blue
* https://flounder.online
* https://sourcehut.org - [Sourcehut Pages](https://sourcehut.org/blog/2021-02-18-sourcehut-pages/)

Meine Gemini-Seiten liegen hier: gemini://schettler.net - ich bin etwas schreibfaul :)
Zum Ansehen brauchst du einen Gemini-Browser. Ich mag [Lagrange](https://gmi.skyjake.fi/lagrange/).

## Seitenstruktur

Der Generator muss wissen, wo die Teile deiner Seiten liegen. Dafür liest er als erstes die Datei `config.yaml` mit Einstellungen. 

Beispiel:

    title: "Hühner & Katzen"
    pages: ./quelle/seiten
    images: ./quelle/bilder
    assets: ./quelle/statisch
    templates: ./templates
    output: ./docs

    image_sizes: 
    - 600
    - 80

    menu:
    - title: Katzen
        href: /
        img: /images/katze-80.jpg
    - title: Hühner
        href: /seite2.html
        img: /images/huhn-80.jpg

Die generierten Seiten liegen unter https://oschettler.github.io/katzen-huehner/

Hier wird die Seite "Hühner & Katzen" in einem Zielordner `output` zusammengestellt. 

Seiten liegen in einem Quellordner im Markdown-Format. Mithilfe von Seitenvorlagen werden daraus HTML-Seiten im Zielordner erzeugt. 

Aus Bildern in einem Quellordner werden quadratische Bilder in verschiedenen Formategrößen im Zielordner erzeugt. 

Dateien aus dem Ordner `assets` werden ohne Änderung in den Zielordner kopiert.    

## Aufruf

Vorbereiten:

    python3 -mvenv env
    source env/bin/activate
    pip install -r requirements.txt

HTML erzeugen:

    ./generate.py

Zielordner leeren:

    ./generate.py clean

Lokal ansehen:

    ./generate.py serve

## Bilder

* https://unsplash.com/photos/7GX5aICb5i4
* https://unsplash.com/photos/auijD19Byq8

## Lizenz

MIT.