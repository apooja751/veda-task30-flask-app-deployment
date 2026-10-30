# Task 30: Deploy a Flask Application on AWS EC2

## Project Overview

This project demonstrates how to deploy a simple Python Flask web application from GitHub to an AWS EC2 Ubuntu virtual machine.

The application is hosted on an EC2 instance and accessed through its public IPv4 address.

## Technologies Used

- AWS EC2
- Ubuntu 24.04 LTS
- Python 3
- Flask
- Git and GitHub
- Python Virtual Environment
- AWS Security Groups

## Architecture

```text
GitHub Repository
       |
       | Git Clone
       v
AWS EC2 Instance
(Ubuntu 24.04)
       |
       v
Python Virtual Environment
       |
       v
Flask Application
       |
       v
Port 5000
       |
       v
Web Browser
```

## Application Features

- Simple Flask web application
- Displays Veda Cloud Internship Task 30 information
- Hosted on an AWS EC2 Ubuntu instance
- Accessible through the instance's public IPv4 address

## Deployment Steps

### 1. Launch EC2 Instance
- Launch an Ubuntu 24.04 LTS EC2 instance.
- Configure a key pair for SSH access.
- Configure the required security group rules.

### 2. Connect to EC2

```bash
ssh -i "veda-task30-key-v2.pem" ubuntu@YOUR_PUBLIC_IP
```

### 3. Install Git and Python Virtual Environment

```bash
sudo apt update
sudo apt install -y git python3-venv
```

### 4. Clone the GitHub Repository

```bash
git clone https://github.com/apooja751/veda-task30-flask-app-deployment.git
cd veda-task30-flask-app-deployment
```

### 5. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 6. Install Dependencies

```bash
pip install -r requirements.txt
```

### 7. Run the Flask Application

```bash
python app.py
```

### 8. Access the Application

Open the following URL in a browser:

http://13.232.2.55:5000

## Security Configuration

The EC2 security group was configured with:

| Type | Port | Purpose |
|---|---:|---|
| SSH | 22 | Remote server access |
| HTTP | 80 | HTTP traffic |
| Custom TCP | 5000 | Flask application access |

SSH access was restricted to the administrator's public IP address.

## Learning Outcomes

- Learned to launch and configure an AWS EC2 instance.
- Practiced SSH-based remote Linux administration.
- Used Git to clone a GitHub repository.
- Created a Python virtual environment.
- Installed Flask dependencies.
- Deployed and accessed a web application on a cloud VM.
- Configured AWS security group rules.

## Note

This project uses Flask's built-in development server for internship demonstration purposes. It is not configured as a production deployment.

