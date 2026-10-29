from fastapi import FastAPI

app = FastAPI(
    title="K8s Production Lab API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Kubernetes Production Lab API",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/api/v1/info")
def info():
    return {
        "application": "k8s-production-lab",
        "version": "1.0.0",
    }