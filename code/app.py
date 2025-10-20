from fastapi import FastAPI
from code.api import routes_task
from code.db.base import Base
from code.db.session import engine

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cloud Task API", version="1.0")
app.include_router(routes_task.router)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "🎉 CICD FastAPI app is live and ready for action!",
        "info": "Use /docs for API documentation and to perform CRUD on task, by /tasks  you can view tasks, and data is persisted in MySQL."
    }

