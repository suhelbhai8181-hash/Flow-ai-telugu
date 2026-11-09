from fastapi import FastAPI

app = FastAPI(title="Flow AI Telugu")

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Flow AI Telugu Backend is running"
    }

@app.get("/health")
def health():
    return {"ok": True}
