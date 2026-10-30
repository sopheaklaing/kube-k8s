# Kubernetes Production Lab

A production-style Kubernetes learning project deployed on an Ubuntu VPS using K3s, Traefik Ingress, Cloudflare Tunnel, and a containerized API.

## 1. Infrastructure Overview

| Component | Configuration |
|---|---|
| VPS | Ubuntu 24.04.5 LTS |
| Kubernetes | K3s v1.36.5 |
| Container Runtime | containerd |
| Ingress Controller | Traefik |
| Public Access | Cloudflare Tunnel |
| Domain | https://api.sopheakdev.online |
| Namespace | k8s-production-lab |
| Deployment | k8s-production-lab-api |
| Replicas | 4 |
| Service Type | ClusterIP |
| Container Port | 8000 |
| Service Port | 80 |

## 2. Architecture

```text
                    Internet Users
                          |
                          v
               Cloudflare Edge / HTTPS
                          |
                          v
                 Cloudflare Tunnel
                          |
                          v
                  Traefik Ingress
                          |
                          v
               Kubernetes Ingress Rule
                          |
                          v
                ClusterIP Service
                          |
             +------------+------------+
             |            |            |
             v            v            v
          API Pod 1    API Pod 2    API Pod 3    API Pod 4
             |            |            |            |
             +------------+------------+------------+
                          |
                          v
                  Kubernetes Node
                     (K3s VPS)
```

## 3. Project Structure

```text
k8s-production-lab/
├── README.md
└── k8s/
    ├── namespace.yaml
    ├── deployment.yaml
    ├── service.yaml
    ├── ingress.yaml
    └── kustomization.yaml
```

## 4. Public API Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | API information |
| `/health` | Health check |

Test:

```bash
curl -i https://api.sopheakdev.online/
curl -i https://api.sopheakdev.online/health
```

## 5. Deploy Kubernetes Resources

Navigate to the Kubernetes directory:

```bash
cd ~/k8s-production-lab/k8s
```

Preview rendered manifests:

```bash
sudo kubectl kustomize .
```

Apply resources:

```bash
sudo kubectl apply -k .
```

## 6. Verify Deployment

```bash
sudo kubectl get nodes -o wide

sudo kubectl get namespaces

sudo kubectl get pods -n k8s-production-lab -o wide

sudo kubectl get deployments -n k8s-production-lab

sudo kubectl get services -n k8s-production-lab

sudo kubectl get ingress -n k8s-production-lab
```

## 7. Resource Monitoring

Check node usage:

```bash
sudo kubectl top nodes
```

Check Pod usage:

```bash
sudo kubectl top pods -n k8s-production-lab
```

## 8. Troubleshooting

Check Pod details:

```bash
sudo kubectl describe pods -n k8s-production-lab
```

Check API logs:

```bash
sudo kubectl logs deployment/k8s-production-lab-api \
  -n k8s-production-lab
```

Follow logs:

```bash
sudo kubectl logs -f deployment/k8s-production-lab-api \
  -n k8s-production-lab
```

Check recent events:

```bash
sudo kubectl get events -n k8s-production-lab \
  --sort-by='.lastTimestamp'
```

## 9. Scaling

Scale API replicas:

```bash
sudo kubectl scale deployment k8s-production-lab-api \
  --replicas=4 \
  -n k8s-production-lab
```

Verify:

```bash
sudo kubectl get deployment,pods -n k8s-production-lab
```

## 10. Restart and Rollout

Restart deployment:

```bash
sudo kubectl rollout restart deployment/k8s-production-lab-api \
  -n k8s-production-lab
```

Check rollout status:

```bash
sudo kubectl rollout status deployment/k8s-production-lab-api \
  -n k8s-production-lab
```

View rollout history:

```bash
sudo kubectl rollout history deployment/k8s-production-lab-api \
  -n k8s-production-lab
```

## 11. Important Production Concepts

- Kubernetes Node and Cluster architecture
- Pods, Deployments, ReplicaSets and Services
- ClusterIP and Ingress networking
- DNS and HTTPS through Cloudflare Tunnel
- Resource Requests and Limits
- Liveness, Readiness and Startup Probes
- Rolling Updates and Rollbacks
- Monitoring and Observability
- RBAC and Kubernetes Security
- High Availability and Disaster Recovery

## 12. Current Infrastructure Limitation

This lab currently uses one VPS and one K3s node.

Although the API has four replicas, all Pods run on the same node. The VPS is therefore a single point of failure.

This is a production-style learning environment, not a highly available production cluster.

Do not use this lab to host critical production workloads without additional reliability, security, backup, and recovery measures.
