#!/bin/bash 
# here will be a bash script for server setup
echo "Starting server setup..."


# assuming linux ubunto
# check update
echo "Updating package list..."
if ! sudo apt update;
then
    echo "failed to update package list"
    exit 1
fi

# install nginx
echo "Installing Nginx..."
if ! sudo apt install -y nginx
then
    echo "failed to install Nginx"
    exit 1
fi
echo "Nginx installed successfully."

echo "Installing pip and pydantic..."
pip install --upgrade pip
pip install pydantic

echo "=== install pydantic done! ==="

#check if process enabled and started
if ! sudo systemctl enable nginx;
then
    echo "failed to enable Nginx"
    exit 1
fi

if ! sudo systemctl start nginx;
then
    echo "failed to start Nginx"
    exit 1
fi
echo "nginx is running"

# check nginx status
echo "Successful exit..."
exit 0