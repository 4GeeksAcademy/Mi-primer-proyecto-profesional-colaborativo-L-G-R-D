"""Comprueba el paquete estático, metadatos, enlaces, recursos y sitemap."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import xml.etree.ElementTree as ET
from urllib.parse import urlsplit, unquote


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.resources, self.errors = set(), [], [], []
        self.counts = {k: 0 for k in ('h1', 'main', 'header', 'footer')}
        self.description = self.canonical = None
        self.language = None
        self.types = []

    def handle_starttag(self, tag, pairs):
        a = dict(pairs)
        if tag in self.counts:
            self.counts[tag] += 1
        if tag == 'html':
            self.language = a.get('lang')
        if a.get('id'):
            if a['id'] in self.ids:
                self.errors.append('ID duplicado: ' + a['id'])
            self.ids.add(a['id'])
        if tag == 'meta' and a.get('name') == 'description':
            self.description = a.get('content')
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical = a.get('href')
        if tag == 'a':
            self.links.append(a.get('href', ''))
        if tag == 'img':
            if any(key not in a for key in ('alt', 'width', 'height')):
                self.errors.append('Imagen sin alt o dimensiones: ' + a.get('src', ''))
            self.resources.append(a.get('src', ''))
        if tag == 'link' and a.get('rel') in ('stylesheet', 'icon', 'preload'):
            self.resources.append(a.get('href', ''))
        if tag == 'source':
            self.resources += [entry.strip().split()[0] for entry in a.get('srcset', '').split(',') if entry.strip()]
        if a.get('itemtype'):
            self.types.append(a['itemtype'])


def check(root):
    root = Path(root).resolve()
    pages = {}
    for file in ('index.html', 'catalogo.html', 'producto.html', 'carrito.html', 'checkout.html'):
        parser = Page()
        parser.feed((root / file).read_text(encoding='utf-8'))
        pages[file] = parser
    errors = []
    for file, page in pages.items():
        errors += [file + ': ' + e for e in page.errors]
        if page.language != 'es' or not page.description:
            errors.append(file + ': idioma/descripción incompletos')
        if any(n != 1 for n in page.counts.values()):
            errors.append(file + ': landmarks o h1 incorrectos')
        for link in page.links + page.resources:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            target_name = unquote(url.path) or file
            target = (root / target_name).resolve()
            if not target.is_relative_to(root) or not target.exists():
                errors.append(file + ': ruta inexistente ' + link)
            elif url.fragment and target_name in pages and url.fragment not in pages[target_name].ids:
                errors.append(file + ': ancla inexistente ' + link)
    if len({p.description for p in pages.values()}) != 5:
        errors.append('Descripciones duplicadas')
    if 'https://schema.org/Organization' not in pages['index.html'].types:
        errors.append('Falta Organization')
    if not {'https://schema.org/Product', 'https://schema.org/Offer'}.issubset(pages['producto.html'].types):
        errors.append('Falta Product/Offer')
    public = (root / 'sitemap.xml').exists()
    if public:
        urls = [e.text for e in ET.parse(root / 'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
        if len(urls) != 3 or any(not p.canonical for p in pages.values()):
            errors.append('Sitemap/canónicas incompletos')
        if any((root / name).exists() for name in ('node_modules', '.git', 'tasks', 'docs', 'package.json')):
            errors.append('La publicación contiene archivos de desarrollo')
    result = {'pages': 5, 'public_build': public, 'errors': errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', nargs='?', default='.')
    raise SystemExit(check(parser.parse_args().directory))
