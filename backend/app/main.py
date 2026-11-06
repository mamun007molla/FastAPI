from fastapi import FastAPI

app = FastAPI(title="Job Tracker")


@app.get("/")
async def home():
    return {"message": "Welcome to the job tracker api"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/about")
async def about():
    return {"app": "job tracker", "version": "1.0"}
