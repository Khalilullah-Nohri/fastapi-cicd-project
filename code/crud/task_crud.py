from sqlalchemy.orm import Session
from code.models.task_model import Task
from code.schemas.task_schema import TaskCreate

def get_all_tasks(db: Session):
    return db.query(Task).all()

def create_task(db: Session, task_data: TaskCreate):
    new_task = Task(**task_data.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None
    db.delete(task)
    db.commit()
    return task


