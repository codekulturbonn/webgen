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

Aus Bildern in einem Quellordner werden verschiedene Formate im Zielordner erzeugt. 

Dateien aus dem Ordner `assets` werden ohne Änderung in den Zielordner kopiert.    

## Aufruf

Vorbereiten:

    python3 -mvenv env
    source env/bin/activate
    pip install -r requirements.txt

HTML erzeugen:

    ./generate.py

Lokal ansehen:

    ./generate.py serve

## Bilder

* https://unsplash.com/photos/7GX5aICb5i4
* https://unsplash.com/photos/auijD19Byq8

## Lizenz

MIT.