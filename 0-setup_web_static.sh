#!/usr/bin/env bash
#Install nignx

sudo apt update
sudo apt install -y nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

html_content="<html>
<head>
<title>Fake HTML</title>
</head>
<body><h1>Fake Hello World</h1></body>
</html>"

echo "$html_content" | sudo tee /data/web_static/releases/test/index.html >/dev/null

current_link="/data/web_static/current"

if [ -L "$current_link" ]; then
    sudo rm "$current_link"
fi

sudo ln -s /data/web_static/releases/test/ "$current_link"

sudo chown -R ubuntu:ubuntu /data/

echo 'server {
	listen 80 default_server;
	listen [::]:80;

	location /hbnb_static/ {
		alias /data/web_static/current/;

	}
}' > /etc/nginx/sites-available/default


sudo service nginx restart
