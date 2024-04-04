#!/usr/bin/env bash
#Install nignx
sudo apt update
sudo apt install nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
html_content="<html>
<head>
<title>Fake HTML</title>
</head>
<body><h1>Fake Hello World</h1></body>
</html>"

echo "$html_content" > /data/web_static/releases/test/index.html

current_link="/data/web_static/current"

if [ -L "$current_link" ]; then
    sudo rm "$current_link"
fi

sudo ln -s /data/web_static/releases/test/ "$current_link"

sudo chown -R ubuntu:ubuntu /data/

echo 'server {
        listen 80 default_server;
        listen [::]:80;

        location /data/web_static/current/ {
                alias hbnb_static;

        }
}' > /etc/nginx/sites-available/default

sudo service nginx restart
