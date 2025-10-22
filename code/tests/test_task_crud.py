import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from code.db.base import Base
from code.crud.task_crud import create_task, get_all_tasks
from code.schemas.task_schema import TaskCreate

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_create_and_get_task(db):
    task_data = TaskCreate(Title="Test Task", Description="This is a test", Completed=False)
    create_task(db, task_data)
    tasks = get_all_tasks(db)
    assert len(tasks) == 1
    assert tasks[0].Title == "Test Task"
