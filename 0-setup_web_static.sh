#!/usr/bin/env bash
# Sets up the web server for the deployment of `web_static`.
if ! command -v nginx &> /dev/null; then
    apt update
    apt install nginx -y
    # sudo systemctl start nginx
    # sudo systemctl enable nginx
fi
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo -e "<html>\n  <head>\n  </head>\n  <body>\nALX\n  </body>\n</html>" > /data/web_static/releases/test/index.html
# echo "<html><body>Hello from ALX</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown ubuntu:ubuntu /data/ -R
if ! grep -q "location /hbnb_static/" /etc/nginx/sites-available/default; then
sed -i '/server_name _;/a\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}' /etc/nginx/sites-available/default
fi
service nginx reload
