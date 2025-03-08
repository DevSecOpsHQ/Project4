# DevSecOps Project 4

This project demonstrates a simple Kubernetes application built with Docker and deployed via GitHub Actions. The code is structured into two main directories:

- **app**: Contains your application code and Dockerfile.
- **kubernetes**: Contains Kubernetes manifests (Deployment & Service).

## Prerequisites

- A Docker Hub account.
- A Kubernetes cluster (e.g., minikube, Docker Desktop with Kubernetes, or a cloud provider).
- [kubectl](https://kubernetes.io/docs/tasks/tools/) installed.
- GitHub Actions enabled in your repository.

### How It Works

1. **CI/CD Pipeline:**
   - On every push to the `main` branch, GitHub Actions:
     - Checks out the repository.
     - Builds a Docker image from the `app` folder.
     - Pushes the image to Docker Hub.
     - Updates the Kubernetes deployment with the new image, triggering a rolling update.

2. **Kubernetes Deployment:**
   - The deployment YAML specifies `imagePullPolicy: Always` so that every new pod pulls the latest image.
   - The service exposes the application on a NodePort, allowing external access.

## Deploying to Kubernetes

### 1. Apply the Manifests

From the project root, run:

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

### 2. Access the Application

- Using minikube:
Run `minikube ip` to get the cluster IP.
Access your app at `http://<minikube-ip>:30080`

- For Docker Desktop with Kubernetes, try accessing the app at:
`http://localhost:<nodePort>`

- If using Amazon EKS:
Because I use a NodePort service for this project, use the public IP or DNS name of one of your EKS worker nodes along with the nodePort:
`http://<node-IP>:<nodePort>`

PS: I chose NodePort for simplicity in Minikube, but Ingress is better for production.
