from pydantic import BaseModel
from typing import List,Dict,Optional
from datetime import datetime


class StoryOptionsSchema(BaseModel):
    text:str
    node_id = Optional[int] = None

class StoryNodeBase(BaseModel):
    content: str
    is_ending: bool = False
    is_winninng_endig: bool = False

class CompleteStoryNodeResponse(StoryNodeBase):
    id: int
    options: List[StoryOptionsSchema] = []

    class Config:
        from_attributes = True

class StoryBase(BaseModel):
    title: str
    session_id:Optional[str] = None

    class Config:
        from_attributes = True

class CreateStoryRequest(BaseModel):
    theme:str
    

class CompleteStoryResponse(StoryBase):
    id: int
    created_at: datetime
    root_node:CompleteStoryNodeResponse
    all_nodes:Dict[int,CompleteStoryNodeResponse]
    

    class Config:
        from_attributes = True

