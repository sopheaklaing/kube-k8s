# Kubernetes Command Cheat Sheet

All commands below assume K3s is installed and `kubectl` is available through `sudo`.

## Cluster

```bash
sudo kubectl cluster-info
sudo kubectl get nodes -o wide
sudo kubectl get namespaces
sudo kubectl get componentstatuses
```

## Workloads

```bash
sudo kubectl get pods -A
sudo kubectl get pods -n k8s-production-lab -o wide
sudo kubectl get deployments -n k8s-production-lab
sudo kubectl get replicasets -n k8s-production-lab
```

## Services and Networking

```bash
sudo kubectl get services -A
sudo kubectl get ingress -A
sudo kubectl get endpoints -n k8s-production-lab
sudo kubectl get ingressclass
```

## Describe and Logs

```bash
sudo kubectl describe pod POD_NAME -n k8s-production-lab
sudo kubectl logs POD_NAME -n k8s-production-lab
sudo kubectl logs -f deployment/k8s-production-lab-api -n k8s-production-lab
sudo kubectl logs POD_NAME --previous -n k8s-production-lab
```

## Resource Monitoring

```bash
sudo kubectl top nodes
sudo kubectl top pods -n k8s-production-lab
sudo kubectl top pods -A
```

## Deployment Management

```bash
sudo kubectl rollout status deployment/k8s-production-lab-api -n k8s-production-lab

sudo kubectl rollout history deployment/k8s-production-lab-api -n k8s-production-lab

sudo kubectl rollout restart deployment/k8s-production-lab-api -n k8s-production-lab

sudo kubectl rollout undo deployment/k8s-production-lab-api -n k8s-production-lab
```

## Scaling

```bash
sudo kubectl scale deployment k8s-production-lab-api --replicas=4 -n k8s-production-lab
```

## Apply YAML / Kustomize

```bash
sudo kubectl diff -k .
sudo kubectl kustomize .
sudo kubectl apply -k .
```

## Troubleshooting

```bash
sudo kubectl get events -n k8s-production-lab --sort-by='.lastTimestamp'
sudo kubectl get pods -n k8s-production-lab
sudo kubectl describe deployment k8s-production-lab-api -n k8s-production-lab
```

## API Tests

```bash
curl -i https://api.sopheakdev.online/
curl -i https://api.sopheakdev.online/health
```

## Important

- `get`, `describe`, `logs`, `top`, `diff`, and `kustomize` are inspection commands.
- `apply`, `scale`, `rollout restart`, and `rollout undo` change cluster state.
- Always inspect the target namespace and resources before changing anything.
- Avoid deleting resources or restarting production services without authorization.
