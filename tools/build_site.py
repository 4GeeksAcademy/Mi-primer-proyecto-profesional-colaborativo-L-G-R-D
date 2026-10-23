"""Genera solo el sitio público y su SEO; no añade JavaScript a la web."""
import argparse
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = ('index.html', 'catalogo.html', 'producto.html', 'carrito.html', 'checkout.html')


class Resources(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('src', 'href'):
            value = attrs.get(key, '')
            if value.startswith('assets/'):
                self.paths.add(value.split('#')[0])
        if tag == 'source':
            for entry in attrs.get('srcset', '').split(','):
                if entry.strip().startswith('assets/'):
                    self.paths.add(entry.strip().split()[0])


def build(base_url, destination):
    parts = urlsplit(base_url)
    if parts.scheme not in ('http', 'https') or not parts.netloc or parts.query or parts.fragment or parts.username:
        raise ValueError('Indica una URL base HTTP(S) completa, sin credenciales, consulta ni fragmento.')
    base = urlunsplit((parts.scheme, parts.netloc, parts.path.rstrip('/') + '/', '', ''))
    destination = Path(destination).resolve()
    # Nunca limpiar recursivamente el repositorio ni una ruta calculada.
    if destination == ROOT or ROOT.is_relative_to(destination):
        raise ValueError('La salida no puede ser el repositorio ni uno de sus directorios padres.')
    destination.mkdir(parents=True, exist_ok=True)
    if any(destination.iterdir()):
        raise ValueError('Usa una carpeta de salida vacía para evitar publicar archivos sobrantes.')
    resources = Resources()
    public_urls = []
    for file in PAGES:
        source = (ROOT / file).read_text(encoding='utf-8')
        resources.feed(source)
        canonical = base if file == 'index.html' else base + file
        title = re.search(r'<title>(.*?)</title>', source).group(1)
        description = re.search(r'<meta name="description" content="([^"]+)"', source).group(1)
        preview = base + ('assets/images/shirt.webp' if file == 'producto.html' else 'assets/images/hero-equipo-desktop.webp')
        tags = [
            f'<link rel="canonical" href="{html.escape(canonical, quote=True)}">',
            '<meta property="og:type" content="website">',
            '<meta property="og:site_name" content="Maison RDL">',
            '<meta property="og:locale" content="es_ES">',
            f'<meta property="og:title" content="{html.escape(html.unescape(title), quote=True)}">',
            f'<meta property="og:description" content="{description}">',
            f'<meta property="og:url" content="{html.escape(canonical, quote=True)}">',
            f'<meta property="og:image" content="{html.escape(preview, quote=True)}">',
            '<meta property="og:image:alt" content="Campaña de demostración Maison RDL">',
            '<meta name="twitter:card" content="summary_large_image">',
        ]
        if file == 'producto.html':
            tags[-2] = '<meta property="og:image:alt" content="Camisa de seda marfil de demostración Maison RDL">'
        if file in ('carrito.html', 'checkout.html'):
            tags.append('<meta name="robots" content="noindex, follow">')
        else:
            public_urls.append(canonical)
        source = source.replace('</head>', '  ' + '\n  '.join(tags) + '\n</head>')
        (destination / file).write_text(source, encoding='utf-8')
    # Incluir únicamente los recursos usados por las páginas y el CSS.
    css = (ROOT / 'assets/css/styles.css').read_text(encoding='utf-8')
    for url in re.findall(r'url\(["\']?([^\)"\']+)', css):
        if not url.startswith(('data:', 'http:', 'https:')):
            resources.paths.add((Path('assets/css') / url).as_posix())
    # Las previsualizaciones sociales se sirven en el mismo sitio.
    resources.paths.update(('assets/images/hero-equipo-desktop.webp', 'assets/images/shirt.webp'))
    for resource in resources.paths:
        source = (ROOT / resource).resolve()
        if not source.is_relative_to(ROOT / 'assets') or not source.is_file():
            raise ValueError(f'Recurso inexistente o fuera de assets: {resource}')
        target = destination / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    # Conservar las licencias de las fuentes publicadas.
    for license_file in (ROOT / 'assets/fonts').glob('*OFL.txt'):
        shutil.copy2(license_file, destination / 'assets/fonts' / license_file.name)
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += ''.join(f'  <url><loc>{html.escape(url)}</loc></url>\n' for url in public_urls)
    (destination / 'sitemap.xml').write_text(sitemap + '</urlset>\n', encoding='utf-8')
    (destination / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {base}sitemap.xml\n', encoding='utf-8')
    (destination / '.nojekyll').touch()
    (destination / 'version.json').write_text(json.dumps({'base_url': base, 'pages': list(PAGES)}, indent=2) + '\n', encoding='utf-8')
    print(f'Sitio público preparado en {destination}; URL base: {base}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-url', required=True)
    parser.add_argument('--output', default='dist')
    args = parser.parse_args()
    build(args.base_url, args.output)
