import staticjinja
import os


url = 'http://localhost:8000'

if os.environ.get('PYCON_ENV') == 'PROD':
    url = 'https://pune.pycon.org/2017'


if __name__ == "__main__":
    site = staticjinja.make_site(
        contexts=[('.*.html', {'url': url})],
    )
    site.render(use_reloader=True)
