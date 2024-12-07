from fastapi import FastAPI
from app.routers.task import router as task_router
from app.routers.user import router as user_router
from app.backend.db import engine, Base

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

print(Base.metadata.tables)


