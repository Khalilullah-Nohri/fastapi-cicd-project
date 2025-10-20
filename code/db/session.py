from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from code.db.base import Base
from code.core.config import settings

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
