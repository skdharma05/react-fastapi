from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from db.database import Base

class Story_job(Base):
    __tablename__ = "story_jobs"

    id = Column(Integer, primary_key=True, index=True)
    job_id= Column(String, unique=True, index=True)
    status = Column(String, index=True)
    session_id = Column(String, index=True)
    theam = Column(String)
    story_id = Column(Integer,nullable=True)
    error = Column(String,nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_job = Column(DateTime(timezone=True),nullable=True)
    
      