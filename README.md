# \# AWS DevOps CI/CD Pipeline Project

# 

# A hands-on DevOps project demonstrating a containerized Flask application, automated CI/CD with Jenkins, Docker image build and push, and Kubernetes deployment.

# 

# \## Project Overview

# 

# This project automates the process of building, testing, packaging, and deploying a Python Flask application using DevOps tools.

# 

# \## Technologies Used

# 

# \- \*\*Python Flask\*\* — Web application

# \- \*\*Docker\*\* — Application containerization

# \- \*\*Jenkins\*\* — CI/CD pipeline automation

# \- \*\*Docker Hub\*\* — Container image registry

# \- \*\*Kubernetes\*\* — Container orchestration and deployment

# \- \*\*Terraform\*\* — Infrastructure as Code configuration

# \- \*\*Git and GitHub\*\* — Version control and source code hosting

# 

# \## Architecture and Workflow

# 

# 1\. Code is stored in the GitHub repository.

# 2\. Jenkins checks out the source code.

# 3\. Jenkins builds the Docker image.

# 4\. Automated tests run against the application.

# 5\. The Docker image is pushed to Docker Hub.

# 6\. Kubernetes manifests are applied to deploy the application.

# 7\. Kubernetes runs two application replicas and exposes the app through a NodePort service.

# 

# \## Project Structure

# 

# ```text

# aws-devops-cicd-project/

# ├── app/

# │   ├── app.py

# │   └── requirements.txt

# ├── tests/

# ├── k8s/

# │   ├── deployment.yaml

# │   └── service.yaml

# ├── terraform/

# │   ├── main.tf

# │   ├── variables.tf

# │   ├── outputs.tf

# │   └── .terraform.lock.hcl

# ├── Dockerfile

# ├── Jenkinsfile

# └── README.md

# ```

# 

# \## Run the Application Locally

# 

# Build the Docker image:

# 

# ```bash

# docker build -t aws-devops-flask:latest .

# ```

# 

# Run the container:

# 

# ```bash

# docker run --rm -p 5000:5000 aws-devops-flask:latest

# ```

# 

# Open `http://localhost:5000` in your browser.

# 

# \## Kubernetes Deployment

# 

# Apply the Kubernetes manifests:

# 

# ```bash

# kubectl apply -f k8s/deployment.yaml

# kubectl apply -f k8s/service.yaml

# ```

# 

# Check the pods and service:

# 

# ```bash

# kubectl get pods

# kubectl get services

# ```

# 

# Application URL:

# 

# `http://localhost:30080`

# 

# Health check:

# 

# `http://localhost:30080/health`

# 

# \## Jenkins CI/CD Pipeline

# 

# The Jenkins pipeline includes these stages:

# 

# \- Checkout source code from GitHub

# \- Check project files and Docker connectivity

# \- Build the Docker image

# \- Run automated tests

# \- Push the image to Docker Hub

# \- Deploy the application to Kubernetes

# \- Verify the Kubernetes rollout

# 

# \## Terraform

# 

# Terraform configuration is included to define the AWS provider, variables, and outputs.

# 

# \*\*Note:\*\* This repository currently contains Terraform configuration only. AWS infrastructure has not been provisioned by this project.

# 

# \## Validation

# 

# \- Flask application runs successfully.

# \- Automated Jenkins pipeline completed successfully.

# \- Docker image was pushed to Docker Hub.

# \- Two Kubernetes pods reached the `Running` state.

# \- Application and health endpoint were accessible locally.

# 

# \## Screenshots

# 

# Screenshots will be added here:

# 

# \- \[ ] Jenkins successful pipeline

# \- \[ ] Docker Hub image

# \- \[ ] Kubernetes pods and service

# \- \[ ] Application homepage

# \- \[ ] Application health endpoint

# 

# \## Skills Demonstrated

# 

# Python, Linux and command-line workflows, Docker, Jenkins, CI/CD, Kubernetes, Git/GitHub, automated testing, and Terraform fundamentals.

# 

# \## Repository

# 

# \[View this project on GitHub](https://github.com/Sahilpaul07/aws-devops-cicd-project)



