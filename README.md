# 🚀 DevOps Flask Automation Platform

Complete DevOps automation project built using:

* Flask
* Docker
* Docker Compose
* Terraform
* AWS EC2
* GitHub Actions
* NGINX Reverse Proxy
* Prometheus
* Grafana
* Loki
* Promtail
* Node Exporter

---

# 🌍 Architecture

```text
Internet
   ↓
NGINX :80
   ↓
Flask App :5000
   ↓
Docker Compose
   ↓
Prometheus :9090
   ↓
Grafana :3000
   ↓
Loki :3100
   ↓
Promtail
```

---

# ⚡ Features

## Flask Automation App

* Bulk Extension Fixer
* Bulk File Renamer
* Video Downloader
* File Sharing System

## DevOps Stack

* Infrastructure as Code using Terraform
* Automated EC2 setup
* Dockerized application
* Auto deployment with GitHub Actions
* Reverse proxy using NGINX
* Monitoring using Prometheus + Grafana
* Centralized logging using Loki + Promtail

---

# 📂 Project Structure

```text
project/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
├── requirements.txt
├── setup.sh
│
├── prometheus/
│   └── prometheus.yml
│
├── loki/
│   └── config.yml
│
├── promtail/
│   └── config.yml
│
├── terraform/
│   └── main.tf
│
├── templates/
│   ├── index.html
│   ├── bulk.html
│   ├── rename.html
│   ├── share.html
│   └── video.html
│
├── modules/
│   ├── bulk_extension_fix.py
│   ├── bulk_rename.py
│   ├── file_share.py
│   └── video_downloader.py
│
└── .github/
    └── workflows/
        └── deploy.yml
```

---

# 🛠 Terraform Setup

## Initialize Terraform

```bash
terraform init
```

## Apply Infrastructure

```bash
terraform apply
```

## Destroy Infrastructure

```bash
terraform destroy
```

---

# ☁ AWS Infrastructure

## Resources Created

* EC2 Instance
* Security Groups
* SSH Key Pair

## Open Ports

| Port | Service       |
| ---- | ------------- |
| 22   | SSH           |
| 80   | NGINX         |
| 5000 | Flask App     |
| 3000 | Grafana       |
| 9090 | Prometheus    |
| 3100 | Loki          |
| 9100 | Node Exporter |

---

# 🐳 Docker Commands

## Build and Start

```bash
docker compose up -d --build
```

## Stop Containers

```bash
docker compose down
```

## Check Running Containers

```bash
docker ps
```

## View Logs

```bash
docker compose logs
```

---

# ⚡ GitHub Actions CI/CD

## Workflow

```text
git push
   ↓
GitHub Actions
   ↓
SSH into EC2
   ↓
git pull
   ↓
docker compose up -d --build
```

## Required GitHub Secrets

| Secret   | Description     |
| -------- | --------------- |
| HOST     | EC2 Public IP   |
| USERNAME | ubuntu          |
| SSH_KEY  | Private SSH Key |

---

# 📊 Monitoring Setup

## Grafana

```text
http://SERVER-IP:3000
```

Default Login:

```text
username: admin
password: admin
```

## Prometheus

```text
http://SERVER-IP:9090
```

## Node Exporter Dashboard

Dashboard ID:

```text
1860
```

---

# 📝 Logging Setup

## Loki

Stores centralized logs.

## Promtail

Collects Docker container logs and sends them to Loki.

## Grafana Logs

Explore → Loki → Query:

```text
{}
```

---

# 🌐 NGINX Reverse Proxy

Application accessible without port:

```text
http://SERVER-IP
```

---

# 🔐 Future Improvements

* HTTPS SSL
* Custom Domain
* Kubernetes
* Jenkins
* SonarQube
* Trivy Security Scanning
* Redis
* PostgreSQL
* Auto Scaling
* AWS ECS/EKS

---

# 👨‍💻 Author

Avitesh Singh

Built for learning complete real-world DevOps workflow using Flask + AWS + Docker + Monitoring + CI/CD.
