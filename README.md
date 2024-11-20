# Web Project with Svelte, FastAPI, and Docker

This project is a full-stack web application with **Svelte** for the frontend, **FastAPI** for the backend, and **Docker** for containerization. 

## Requirements

Before you begin, ensure you have the following software installed:

- **Node.js** (v18+): Required to run the frontend application with Svelte.
- **Python** (v3.8+): Required for the backend FastAPI server.
- **Git**: For version control and managing the project repository.
- **Docker Desktop**: To build and run Docker containers for both the frontend and backend.

## Installation

To set up this project locally, follow these steps:

### Git installation

```bash
git --version #verify if you have git installed already
sudo apt update
sudo apt install git
```

### Git Post Install

```bash
git config --global user.email "youremail@example.com"
git config --global user.name "Your Name"
```

### Python Installation

```bash
python3 --version #verify if you have python installed already
sudo apt update
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-venv
```

### Node Installation

```bash
sudo apt install curl
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
nvm install --lts
node -v
npm -v
```

### Docker Desktop Installation

```bash
sudo apt update
sudo apt install certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
curl 'https://desktop.docker.com/linux/main/amd64/docker-desktop-amd64.deb?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-linux-amd64' -o dockerDesktop.deb #If downloading the .deb via cli do not work go directly to the link with your browser
sudo apt install./dockerDesktop.deb
```

## Setup Project

First you will need to clone the repo.

### Start Front Command

```bash
npm i
npm run dev
```

### Start Back Command
```
python3 -m venv myenv
source ./myenv/bin/activate
pip install "fastapi[standard]"
fastapi dev main.py
```

## Docker Command Reminder

### To build an image

```bash
docker build -t "Image Name"
```

### To run a container using an image

```bash
docker run -d --name "Container Name" "Image Name"
```

### Build with docker compose

```bash
docker compose build
```

### Run All Containers with docker compose

```bash
docker compose up -d
```

### Show docker images
```bash
docker images
```

### Manage docker containers
```bash
docker ps
docker stop "container_id"
docker rm "container_id"
```
