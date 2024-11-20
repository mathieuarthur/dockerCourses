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
```

### Node Installation

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
nvm install --lts
node -v
npm -v
```

### Docker Desktop Installation

WIP

## Setup Project

First you will need to clone the repo.

### Start Front Command

```bash
npm i
npm run dev
```

### Start Back Command
```
pip install -r requirements.txt
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


