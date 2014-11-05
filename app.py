import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

from domains import DOMAINS

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

@app.route('/<path:site>/index.html')
def page(site):
    page = pages.get_or_404(site)
    return render_template('page.html', page=page)

@freezer.register_generator
def page():
    for site in DOMAINS:
        yield {'site': site}

#def image_url(filename):
#    return filename

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(port=8000)
