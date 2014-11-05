import os
import sys

from jinja2 import Environment, PackageLoader

from domains import DOMAINS

FOLDER = './sites-enabled/'

def do_clear():
    for fpath in os.listdir(FOLDER):
        fpath = os.path.join(FOLDER, fpath)
        try:
            if os.path.isfile(fpath):
                os.unlink(fpath)
        except Exception, e:
            print e

def do_build():
    env = Environment(loader=PackageLoader(__name__, 'templates'))
    template = env.get_template('nginx.conf')
    for domain in DOMAINS:
        fpath = os.path.join(FOLDER, domain)
        with open(fpath, 'w') as f:
            f.write(template.render(domain=domain))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "clear":
            do_clear()
        elif sys.argv[1] == "build":
            do_build()
    else:
        print "usage: %s %s" % (sys.argv[0], "[build|clear]")
