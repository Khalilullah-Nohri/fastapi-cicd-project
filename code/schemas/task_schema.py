from pydantic import BaseModel

class TaskBase(BaseModel):
    Title: str
    Description: str | None = None
    Completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int

    class ConfigDict:
        orm_mode = True
