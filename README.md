# EKS Blue/Green Deployment with ArgoCD + Helm

This project demonstrates a blue/green deployment strategy on Amazon EKS using GitOps with ArgoCD and Helm.

## 🛠️ Tech Stack
- AWS EKS
- Kubernetes
- Helm
- ArgoCD
- Docker
- Flask (sample app)

## 🚀 Architecture
- Two parallel deployments: `blue` and `green`
- ArgoCD watches Helm manifests in GitHub
- Traffic is manually switched between blue and green via Ingress

## 📂 Repo Structure
- `charts/myapp`: Helm chart
- `argocd/`: ArgoCD Application YAMLs
- `app/`: Flask app
- `Dockerfile`: App image

## 🎯 Deployment Steps
1. Deploy EKS and install ArgoCD
2. Push manifests to GitHub
3. ArgoCD syncs and deploys blue/green apps
4. Route traffic using Ingress

## 📸 Screenshots
Add ArgoCD UI snapshots + `curl` output showing blue/green switch

## 🔁 Rollbacks
To roll back, just sync the other environment or reset Ingress rule