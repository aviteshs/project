#!/bin/bash

# Logs
exec > /var/log/user-data.log 2>&1

# Update System
apt update -y
apt upgrade -y

# Install Basic Packages
apt install -y git python3 python3-pip python3-venv ca-certificates curl


mkdir -p /home/ubuntu/.ssh

cat <<EOF >> /home/ubuntu/.ssh/authorized_keys
${public_key}
EOF

chmod 700 /home/ubuntu/.ssh
chmod 600 /home/ubuntu/.ssh/authorized_keys

chown -R ubuntu:ubuntu /home/ubuntu/.ssh

# -----------------------------
# Install Docker (Official)
# -----------------------------

install -m 0755 -d /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

chmod a+r /etc/apt/keyrings/docker.asc

tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: jammy
Components: stable
Architectures: amd64
Signed-By: /etc/apt/keyrings/docker.asc
EOF

# Update Again
apt update -y

# Install Docker
apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Start Docker
systemctl start docker
systemctl enable docker

# -----------------------------
# Clone Project
# -----------------------------

cd /

git clone https://github.com/aviteshs/project.git

cd /project

# -----------------------------
# Build Docker Image
# -----------------------------

docker build -t myapp .

# -----------------------------
# Run Container
# -----------------------------

docker run -d -p 5000:5000 --name mycontainer myapp