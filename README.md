# 🚀 Python Flask CI/CD Pipeline using Jenkins, Docker & Kubernetes (EKS)

This project demonstrates a complete end-to-end CI/CD pipeline where a Python Flask application is built, containerized, pushed to Docker Hub, and deployed to Kubernetes (EKS) using Jenkins.

------------------------------------------------------------

## 🏗️ Architecture Flow

GitHub → Jenkins → Docker → Docker Hub → Kubernetes (EKS)

1. Jenkins clones the GitHub repository using SCM.
2. Jenkins builds a Docker image from the Dockerfile.
3. The Docker image is pushed to Docker Hub.
4. Kubernetes pulls the image from Docker Hub.
5. The application is deployed using Deployment and NodePort Service.

------------------------------------------------------------

## 📁 Project Structure

python-flask-cicd-kubernetes/
│
├── app.py  
├── requirements.txt  
├── Dockerfile  
├── deployment.yml  
├── service.yml  
├── Jenkinsfile  
└── README.md  

------------------------------------------------------------

## 🐍 Application Details

- Python Flask based web application
- Runs on port 5000
- Custom UI with DevOps & Multi-Cloud theme
- Displays:
  - DevOps With Multi Cloud
  - Presented by Veera Sir
  - Team VeeraOps

------------------------------------------------------------

## 🐳 Docker Setup

Dockerfile configuration:
- Base image: python:3.9-slim
- Copies requirements.txt
- Installs dependencies
- Copies application code
- Exposes port 5000
- Runs app.py

Manual build command:
docker build -t your-dockerhub-username/python-flask-app:latest .

Push command:
docker push your-dockerhub-username/python-flask-app:latest

------------------------------------------------------------

## ⚙️ Jenkins Setup (Amazon Linux EC2)

1. Installed Jenkins
2. Installed Docker
3. Started Docker service:
   sudo systemctl start docker
   sudo systemctl enable docker

4. Added Jenkins user to Docker group:
   sudo usermod -aG docker jenkins
   sudo reboot

5. Configured GitHub repository in Jenkins using SCM
6. Added Docker Hub credentials inside Jenkins

------------------------------------------------------------

## 📦 Jenkins Pipeline Stages

1. Checkout SCM (GitHub repository clone)
2. Build Docker image
3. Login to Docker Hub
4. Push Docker image to Docker Hub
5. Deploy to Kubernetes using kubectl apply

------------------------------------------------------------

## ☸️ Kubernetes Deployment

### Deployment.yml
- Creates 2 replicas
- Pulls Docker image from Docker Hub
- Container runs on port 5000

### Service.yml
- Type: NodePort
- Exposes application externally
- Example NodePort: 30007

------------------------------------------------------------

## 🔎 Kubernetes Commands Used

Check nodes:
kubectl get nodes

Check pods:
kubectl get pods

Check services:
kubectl get svc

Describe service:
kubectl describe svc flask-service

Check logs:
kubectl logs <pod-name>

------------------------------------------------------------

## 🔐 Kubernetes Authentication Fix

Since Jenkins runs as a separate user, kubeconfig was copied:

sudo mkdir -p /var/lib/jenkins/.kube
sudo cp /root/.kube/config /var/lib/jenkins/.kube/
sudo chown -R jenkins:jenkins /var/lib/jenkins/.kube

------------------------------------------------------------

## 🌍 Access Application

http://<EC2-Public-IP>:30007

------------------------------------------------------------

## 🧠 Issues Faced & Resolutions

1. Git branch mismatch (master → main)
2. Docker daemon permission issue
3. Jenkins user not in Docker group
4. Kubernetes authentication error (Forbidden)
5. Missing requirements.txt during Docker build

All issues were successfully resolved.

------------------------------------------------------------

## 🎯 Final Outcome

✔ Repository cloned via Jenkins SCM  
✔ Docker image built successfully  
✔ Image pushed to Docker Hub  
✔ Kubernetes pulled image  
✔ Application deployed using Deployment & NodePort  
✔ Flask app accessible via browser  

------------------------------------------------------------

## 🛠️ Tech Stack

- Python Flask
- Docker
- Jenkins
- Docker Hub
- Kubernetes (EKS)
- Amazon Linux EC2

------------------------------------------------------------

## 👨‍💻 Author

Deepak Kalal  
DevOps With Multi Cloud  
Team VeeraOps 🚀
