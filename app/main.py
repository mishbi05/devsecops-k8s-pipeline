from fastapi import FastAPI

app = FastAPI(title="Cloud DevOps Microservice", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Hello from DevSecOps Pipeline!", "status": "running"}

@app.get("/healthz")
def health_check():
    return {"status": "healthy"}

@app.get("/ready")
def readiness_check():
    return {"status": "ready"}
