Application to be used with the following Dockerfile

    # Dockerfile
    FROM dockerfile/ubuntu

    # Install Nginx.
    RUN \
      add-apt-repository -y ppa:nginx/stable && \
      apt-get update && \
      apt-get install -y nginx && \
      rm -rf /var/lib/apt/lists/* && \
      echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
      chown -R www-data:www-data /var/lib/nginx

    # Define mountable directories.
    VOLUME ["/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx"]

    # Define working directory.
    # WORKDIR /etc/nginx

    # Expose ports.
    EXPOSE 80
    EXPOSE 443

    # Set working directory for application.
    RUN mkdir -p /root/src
    WORKDIR /root/src

    # Install Python then clone gs-satellite.
    RUN \
      echo "deb http://archive.ubuntu.com/ubuntu/ trusty main universe" >> /etc/apt/sources.list && \
      apt-get update && \
      apt-get install -y git python python-dev python-distribute python-pip && \
      git clone https://github.com/teisman/gs-satellite.git

    WORKDIR gs-satellite

    # Build and set-up pages and Nginx-configs.
    RUN \
      pip install -r requirements.txt && \
      python nginx-conf.py build && \
      mkdir -p /etc/nginx/sites-enabled &&\
      cp ./sites-enabled/* /etc/nginx/sites-available/ && \
      ln -sf /etc/nginx/sites-available/* /etc/nginx/sites-enabled/ && \
      # rm /etc/nginx/sites-enabled/default && \
      # rm /etc/nginx/sites-available/default && \
      python app.py build && \
      mkdir -p /usr/share/nginx/www && \
      cp -r ./build/* /usr/share/nginx/www/ && \
      cp -r ./static/* /usr/share/nginx/www/

    # Define default command.
    CMD ["nginx"]

