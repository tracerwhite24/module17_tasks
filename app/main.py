from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routers.task import router as user_router

app = FastAPI()

@app.get("/")
async def root():
    return JSONResponse(content={"message": "Welcome to Taskmanager"})

app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
