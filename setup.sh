#!/bin/bash

exec > /var/log/user-data.log 2>&1

apt update -y
apt upgrade -y

# Install Packages
apt install git -y
apt install python3 -y
apt install python3-pip -y
apt install python3-venv -y

# Move to Root
cd /

# Clone Repo
git clone https://github.com/aviteshs/project.git

# Go Inside Project
cd /project

# Create Venv
python3 -m venv venv

# Install Requirements
./venv/bin/pip install -r requirements.txt

# Run Flask App
nohup ./venv/bin/python3 app.py > app.log 2>&1 &