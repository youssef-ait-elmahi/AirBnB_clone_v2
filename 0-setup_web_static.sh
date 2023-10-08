#!/usr/bin/env bash
#Upgrading nginx configuration

# Install nginx if not already installed
if ! command -v nginx &> /dev/null;
then
sudo apt-get update
sudo apt-get -y install nginx
sudo service nginx start
fi

#Create directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#Create html file
sudo sh -c 'echo "Hello World!" > /data/web_static/releases/test/index.html'

#Symbolic link 
source_path="/data/web_static/releases/test/"
symlink_path="/data/web_static/current"
if [ -h "$symlink_path" ]; then
    rm "$symlink_path"
fi

#Link paths symbolinkly
sudo ln -s "$source_path" "$symlink_path"

#Give user/group permission to ubuntu
sudo chown -R ubuntu:ubuntu /data/
sudo chgrp -R ubuntu /data/

#Update the Nginx configuration to serve the content
df_path="/etc/nginx/sites-available/default"
new_loc="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "/^\tserver_name _;/a\\$new_loc" $df_path
sudo service nginx restart