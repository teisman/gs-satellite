server {
    server_name www.hello-world.com;
    rewrite ^(.*) http://hello-world.com$1 permanent;
}

server {
    listen 80 default;

    server_name hello-world.com;

    root /usr/share/nginx/www/hello-world.com;
    index index.html index.htm;


    access_log  /var/log/nginx/hello-world.com/access.log;
    error_log  /var/log/nginx/hello-world.com/error.log;
}