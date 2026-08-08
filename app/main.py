from fastapi import FastAPI

app = FastAPI(
    title="Smart Textile Manufacturing Platform",
    description="API for textile quality inspection and production monitoring",
    version="1.0.0",
)


@app.get("/")
def home():
    return {"message": "Smart Textile Manufacturing Platform API is running"}


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Smart Textile Manufacturing Platform"
    }


@app.get("/production")
def production_status():
    return {
        "machine": "Textile Machine 01",
        "production_rate": 85,
        "downtime": 5,
        "status": "Running",
    }


@app.get("/defects")
def defect_summary():
    return {
        "fabric_roll": "ROLL-001",
        "defects_detected": 3,
        "defect_types": ["Stain", "Weaving Fault", "Stitching Error"],
    }
