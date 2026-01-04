# Process Documentation: AI-Powered Resume Screening Tool

## Overview

This document provides a comprehensive, step-by-step record of the Unix/Linux commands used during the development, containerization, CI/CD setup, and deployment of the AI-Powered Resume Screening Tool. It serves as a reference for reproducing the environment and processes.

## Table of Contents

- [Step 0: System Preparation (Ubuntu)](#step-0-system-preparation-ubuntu)
- [Step 1: Install Python & Dependencies](#step-1-install-python--dependencies)
- [Step 2: Git Repository Setup](#step-2-git-repository-setup)
- [Step 3: Docker Installation & Setup](#step-3-docker-installation--setup)
- [Step 4: Docker Permissions Fix](#step-4-docker-permissions-fix)
- [Step 5: Docker Image Build & Test](#step-5-docker-image-build--test)
- [Step 6: Jenkins Installation & Management](#step-6-jenkins-installation--management)
- [Step 7: Jenkins Pipeline Execution](#step-7-jenkins-pipeline-execution)
- [Step 8: Fix Python PEP 668 Issue](#step-8-fix-python-pep-668-issue)
- [Step 9: Docker Hub Authentication & Push](#step-9-docker-hub-authentication--push)
- [Step 10: CI/CD File Management](#step-10-cicd-file-management)
- [Step 11: Verification & Monitoring](#step-11-verification--monitoring)

## Step 0: System Preparation (Ubuntu)

Update system packages:

```bash
sudo apt update
sudo apt upgrade -y
```

Install essential tools:

```bash
sudo apt install -y git curl wget unzip
```

## Step 1: Install Python & Dependencies

Check Python version:

```bash
python3 --version
```

Install Python tools:

```bash
sudo apt install -y python3-pip python3-venv
```

Create requirements file:

```bash
pip freeze > requirements.txt
```

## Step 2: Git Repository Setup

Clone project repository:

```bash
git clone https://github.com/sumanbiswas15/resume_screening_tool.git
cd resume_screening_tool
```

Check Git status:

```bash
git status
```

Add and commit files:

```bash
git add .
git commit -m "Initial project setup"
```

Push to GitHub:

```bash
git push origin main
```

## Step 3: Docker Installation & Setup

Install Docker:

```bash
sudo apt install -y docker.io
```

Start and enable Docker service:

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

Verify Docker installation:

```bash
docker --version
docker ps
```

## Step 4: Docker Permissions Fix

Add user to Docker group:

```bash
sudo usermod -aG docker Suman
sudo usermod -aG docker jenkins
```

Apply group changes:

```bash
newgrp docker
```

Verify Docker group members:

```bash
getent group docker
```

Restart Jenkins after permission change:

```bash
sudo systemctl restart jenkins
```

## Step 5: Docker Image Build & Test

Build Docker image:

```bash
docker build -t resume-screening-app .
```

Run Docker container:

```bash
docker run -p 8501:8501 resume-screening-app
```

Verify running containers:

```bash
docker ps
```

## Step 6: Jenkins Installation & Management

Install Jenkins:

```bash
sudo apt install -y jenkins
```

Start Jenkins:

```bash
sudo systemctl start jenkins
```

Check Jenkins status:

```bash
sudo systemctl status jenkins
```

Switch to Jenkins user:

```bash
sudo su - jenkins
```

Exit Jenkins user:

```bash
exit
```

## Step 7: Jenkins Pipeline Execution

Jenkins automatically executed the following actions via Jenkinsfile:

- Git repository checkout
- Dependency installation
- Test execution
- Docker image build

Manual verification commands:

```bash
docker ps
docker images
```

## Step 8: Fix Python PEP 668 Issue

Create Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies inside venv:

```bash
pip install -r requirements.txt
```

Deactivate environment:

```bash
deactivate
```

## Step 9: Docker Hub Authentication & Push

Login to Docker Hub:

```bash
docker login
```

Tag Docker image:

```bash
docker tag resume-screening-app sumanbiswas22/resume-screening-app
```

Push image:

```bash
docker push sumanbiswas22/resume-screening-app
```

## Step 10: CI/CD File Management

Create CI files:

```bash
nano Jenkinsfile
nano Dockerfile
nano .gitlab-ci.yml
```

Commit CI/CD files:

```bash
git add Jenkinsfile Dockerfile .gitlab-ci.yml
git commit -m "Add CI/CD pipeline and Docker support"
git push origin main
```

## Step 11: Verification & Monitoring

Check Jenkins logs:

```bash
journalctl -u jenkins
```

Check Docker daemon:

```bash
sudo systemctl status docker
```
