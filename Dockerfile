FROM dockerfile/nginx

RUN \
  apt-get install -y git python-virtualenv && \
  git clone <repo> . && \
  pip install -r requirements.txt && \
  python nginx.py build && \
  ln -s ./sites-enabled/* /etc/nginx/sites-enabled/ && \
  python site.py build && \
  ln -s ./build/* /usr/share/nginx/www/
