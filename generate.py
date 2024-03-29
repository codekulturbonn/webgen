#!/usr/bin/env python3

'''
Einfacher Generator für statische Websites

- Seiten in Markdown-Dateien mit Frontmatter
- Vorlagen im Mustache-Format
- Bilder werden in verschiedene Größen verkleinert
'''

import chevron
import frontmatter
import functools
import http.server
import markdown
import os
from PIL import Image, ImageOps
import re
import shutil
import sys
import webbrowser
import yaml

config = {}
templates = {}
pages = []

def load_config():
    '''
    Einstellungen aus Datei config.yaml lesen
    '''
    global config
    config = yaml.load(open('config.yaml'), Loader=yaml.Loader)


def load_templates():
    '''
    Seitenvorlagen lesen
    '''
    global templates

    dir = config['templates']
    for filename in os.listdir(dir):
        if not filename.endswith('.mustache'):
            continue
        name = os.path.splitext(filename)[0]
        templates[name] = open(os.path.join(dir, filename)).read()


def collect_pages(root_dir, dir = '.'):
    global pages

    source_dir = os.path.join(root_dir, dir)
    out_dir = os.path.join(config['output'], dir)
    os.makedirs(out_dir, exist_ok=True) 
    
    with os.scandir(source_dir) as it:
        for entry in it:
            if entry.name.startswith('.'):
                continue
            if entry.is_dir():
                collect_pages(root_dir, os.path.join(dir, entry.name))
            else:
                source_path = os.path.join(source_dir, entry.name)
                print("SOURCE", source_path)

                basename = os.path.splitext(entry.name)[0]
                if entry.name.endswith('.md'):
                    out_filename = basename + '.html'
                    out_path = os.path.join(out_dir, out_filename)

                    article = frontmatter.load(source_path)
                    pages.append({
                        'source_path': source_path,
                        'out_path': out_path,
                        'dir': dir,
                        'basename': basename,
                        'is_index': basename == 'index',
                        'in_menu': basename != 'index' and not ('hide' in article.metadata and article.metadata['hide']),  
                        'filename': out_filename,
                        'meta': article.metadata
                    })
                elif entry.name.endswith('~'):
                    continue
                else:
                    out_path = os.path.join(out_dir, entry.name)
                    pages.append({
                        'source_path': source_path,
                        'out_path': out_path,
                        'dir': dir,
                        'basename': basename,
                        'is_index': basename == 'index',
                        'in_menu': False,
                        'filename': entry.name,
                    })


def generate_pages():
    '''
    HTML-Seiten erzeugen und ins Zielverzeichnis kopieren. 
    
    Dateien im Markdown-Format werden nach HTML gewandelt und
    über die Seitenvorlage 'article' in eine vollständige 
    HTML-Datei mit Kopf und Fuß gewandelt.
    '''

    for page in pages:
        
        source_path = page['source_path']
        out_path = page['out_path']
        
        if 'meta' in page:
            print(f"Generiere {out_path}")

            with open(out_path, 'w') as out:
                article = frontmatter.load(source_path)

                if 'filter' in page['meta']:
                    mod = __import__(page['meta']['filter'], fromlist=[None])
                    filter = getattr(mod, 'filter')
                    page['meta'] = filter(page['meta'], config=config)

                rendered_markdown = markdown.markdown(article.content)
                content = chevron.render(
                    template=re.sub('{{&gt;', '{{>', rendered_markdown),
                    partials_path='partials/',
                    data={
                        'page': page,
                        'site': config,
                        'pages': pages
                    },
                    warn=True
                )

                template = page['meta']['template'] if 'template' in page['meta'] else 'article'
                html = chevron.render(
                    template=templates[template],
                    partials_path='partials/',
                    data={
                        'page': page,
                        'site': config,
                        'content': content,
                        'pages': pages
                    },
                    warn=True
                )
                out.write(html)
        else:
            print(f"Kopiere {out_path}")
            shutil.copyfile(source_path, out_path)



def generate_images(root_dir, dir = '.'):
    '''
    Bilder in verschiedene Größen verkleinern und ins Zielverzeichnis kopieren.
    '''
    source_dir = os.path.join(root_dir, dir)
    out_dir = os.path.join(config['output'], 'images', dir)
    os.makedirs(out_dir, exist_ok=True) 
    
    with os.scandir(source_dir) as it:
        for entry in it:
            if entry.name.startswith('.'):
                continue
            if entry.is_dir():
                generate_images(root_dir, os.path.join(dir, entry.name))
            else:
                source_path = os.path.join(source_dir, entry.name)
                source_mtime = os.stat(source_path).st_mtime

                base, ext = os.path.splitext(entry.name)

                for size in config['image_sizes']:
                    out_path = os.path.join(out_dir, base + '-' + str(size) + ext)
                    try:
                        if os.stat(out_path).st_mtime > source_mtime:
                            continue
                    except:
                        pass

                    print(f"Bild {out_path}")

                    try:
                        image = Image.open(source_path)
                        #image.thumbnail((size, size))
                        thumb = ImageOps.fit(image, (size, size), Image.ANTIALIAS)
                        thumb.save(out_path)
                    except:
                        print(f"Konnte Bild {source_path} nicht verkleinern")

if __name__ == '__main__':
    load_config()

    if len(sys.argv) == 2:
        if sys.argv[1] == 'serve':
            # Wenn 'serve' angegeben, starte einen Webserver und öffne den Browser
            port = 8000
            print(f'Webserver auf http://localhost:{port}')
            webbrowser.open(f'http://localhost:{port}')
            handler = functools.partial(
                http.server.SimpleHTTPRequestHandler, directory=config['output']
            )
            httpd = http.server.HTTPServer(('', port), handler)
            httpd.serve_forever()

        elif sys.argv[1] == 'clean':
            shutil.rmtree(config['output'])

    else:
        # Sonst wandle Seiten, Bilder und kopiere sie zusammen mit den statischen Dateien 
        load_templates()
        collect_pages(config['pages'])
        print(yaml.dump(pages))

        shutil.copytree(config['assets'], config['output'], dirs_exist_ok=True)

        generate_pages()
        generate_images(config['images'])

