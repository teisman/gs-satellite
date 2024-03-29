import os
import glob
import sys

from jinja2 import Environment, PackageLoader

domains = glob.glob('pages/*')
domains = [os.path.split(domain)[1] for domain in domains]

PATH = './sites-enabled/'

def do_clear():
    for fpath in os.listdir(PATH):
        fpath = os.path.join(PATH, fpath)
        try:
            if os.path.isfile(fpath):
                os.unlink(fpath)
        except Exception, e:
            print e

def do_build():
    env = Environment(loader=PackageLoader(__name__, 'templates'))
    template = env.get_template('nginx.conf')
    for domain in domains:
        fpath = os.path.join(PATH, domain)
        with open(fpath, 'w') as f:
            f.write(template.render(domain=domain))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        if not os.path.exists(PATH):
            os.makedirs(PATH)
        do_clear()
        do_build()
    else:
        print "usage: %s %s" % (sys.argv[0], "[build|clear]")
