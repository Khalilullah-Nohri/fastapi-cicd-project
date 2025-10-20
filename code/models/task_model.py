from sqlalchemy import Column, Integer, String, Boolean
from code.db.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    Title = Column(String(100), nullable=False)
    Description = Column(String(255))
    Completed = Column(Boolean, default=False)
