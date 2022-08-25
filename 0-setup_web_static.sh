#!/usr/bin/env bash
#Deployment of web static.

if [ "$(dpkg-query -W -f="${Status}" nginx 2>/dev/null | grep -c "ok installed")" -eq 0 ]
then
  apt-get update;
  apt-get -y install nginx;
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i '/^\terror_page 404 \/error404.html;/a \\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current/;\n\t}' /etc/nginx/sites-available/default
service nginx restart
