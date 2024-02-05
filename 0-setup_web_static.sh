#!/usr/bin/env bash
#Setting up webservice
if ! command -v nginx &> /dev/null; then
    echo "Installing Nginx..."
    sudo apt-get update
    sudo apt-get install -y nginx
fi
sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir -p "/data/web_static/shared/"

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

nginx_config="/etc/nginx/sites-available/default"

echo "location /hbnb_static/ {
    alias /data/web_static/current/;
    index index.html index.htm;  # Add this line if necessary
}" | sudo tee -a "$nginx_config" > /dev/null

sudo service nginx restart
