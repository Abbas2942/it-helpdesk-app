
# IT Help Desk Application

A simple IT Help Desk web application built using Python Flask, Docker, and Kubernetes.

## Project Overview

This project demonstrates how to build, containerize, deploy, and troubleshoot a web application in Kubernetes.

IT engineers can create and view tickets for server issues.

## Technologies Used

- Python Flask — Backend application
- HTML and CSS — Frontend website
- SQLite — Database
- Docker — Container image
- Kubernetes — Container orchestration
- Minikube — Local Kubernetes cluster
- GitHub — Source code management
- VS Code — Development environment

## Features

- Create IT support tickets
- Enter a server name and issue
- Select Low, Medium, or High priority
- View submitted tickets
- Track ticket status as Open
- Health-check endpoint

## Architecture

User Browser
    |
    v
Kubernetes Service
    |
    v
IT Help Desk Pod
    |
    v
Python Flask Application
    |
    v
SQLite Database

## How to Deploy

### 1. Clone the Repository

git clone https://github.com/Abbas2942/it-helpdesk-app.git

cd it-helpdesk-app

### 2. Start Minikube

minikube start

### 3. Build Docker Image

minikube image build -t it-helpdesk:v1 .

### 4. Create Namespace

kubectl create namespace helpdesk

### 5. Deploy Application

kubectl apply -f k8s/ -n helpdesk

### 6. Check Kubernetes Resources

kubectl get pods -n helpdesk

kubectl get deployments -n helpdesk

kubectl get svc -n helpdesk

### 7. Access the Website

kubectl port-forward -n helpdesk svc/it-helpdesk 8080:5000

Open in your browser:

http://localhost:8080

## Kubernetes Troubleshooting

Check Pod status:

kubectl get pods -n helpdesk -o wide

View application logs:

kubectl logs deployment/it-helpdesk -n helpdesk

Check deployment details:

kubectl describe deployment it-helpdesk -n helpdesk

Check Kubernetes events:

kubectl get events -n helpdesk

## Screenshot

![IT Help Desk Website](screenshots/helpdesk.png)

## Important Notes

This project uses SQLite with temporary Kubernetes storage. Ticket data may be lost when the Pod is replaced.

The application is intended for local development and Kubernetes learning, not production use.

## What I Learned

- Building a Python web application
- Creating Docker images
- Writing Kubernetes YAML files
- Deploying applications using kubectl
- Using Kubernetes Services
- Troubleshooting Pods and logs
- Using Git and GitHub to manage code

## Author

GitHub: Abbas2942
