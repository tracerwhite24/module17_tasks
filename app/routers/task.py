from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/task", tags=["task"])

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

@router.get("/")
async def all_tasks():
    pass

@router.get("/{task_id}")
async def task_by_id(task_id: int):
    pass

@router.post("/create", response_model=Task)
async def create_task(task: TaskCreate):
    pass

@router.put("/update/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskUpdate):
    pass

@router.delete("/delete/{task_id}")
async def delete_task(task_id: int):
    pass
