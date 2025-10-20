from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# from code.db.session import get_db
from code.db.session import SessionLocal
from code.crud.task_crud import create_task, get_all_tasks, delete_task
from code.schemas.task_schema import TaskCreate, TaskResponse

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all tasks
@router.get("/", response_model=list[TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return get_all_tasks(db)

# POST create task
@router.post("/", response_model=TaskResponse)
def add_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)

# DELETE task
@router.delete("/{task_id}", response_model=TaskResponse)
def remove_task(task_id: int, db: Session = Depends(get_db)):
    deleted = delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted
