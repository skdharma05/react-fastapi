import uuid
from  typing import Optional
from datetime import datetime
from fastapi import APIRouter,Depends,HTTPException,Cookie,Response,BackgroundTasks
from sqlalchemy.orm import Session

from db.database import get_db,SessionLocal
from models.story import Story , StoryNode
from models.job import Story_job
from schemas.story import(
    CompleteStoryNodeResponse,CompleteStoryResponse, CreateStoryRequest

)
from schemas.job import StoryJobResponse


router = APIRouter(
    prefix="/stories",
    tags=["stories"]
)


def get_session_id(session_id:Optional[str]=Cookie(None)):
    if not session_id:
        session_id=str(uuid.uuid4())
    return session_id


@router.post("/create",response_model=StoryJobResponse)
def create_story(
    request:CreateStoryRequest,
    background_task : BackgroundTasks,
    session_id= Depends(get_session_id),
    db :Session = Depends(get_db)
):
    Response.set_cookie(key="session_id",value=session_id,httponly=True)

    job_id = str(uuid.uuid4())

    job = Story_job(
        job_id= job_id,
        session_id= session_id,
        theme= request.theme,
        status = "pending"
                )
    db.add(job)
    db.commit()


    background_task.add_task(
        generate_story_task,
        job_id = job_id,
        theme= request.theme,
        session_id = session_id
    )

    return job

def generate_story_task(job_id:str,theme:str,session_id:str):
    db= SessionLocal()

    try:
        job= db.query(Story_job).filter(Story_job.job_id==job_id).first()

        if not job:
            return
        
        try:
            job.status="processing"
            db.commit()

            story = {}  # todo generate story 

            job.story_id=1 # todo : update id
            job.status="completed"
            job.completed_job = datetime.now()
            db.commit()
        except Exception as e:
            job.status="failed"
            job.completed_job = datetime.now()
            job.error=str(e)
            db.commit()
    finally:
        db.close()


