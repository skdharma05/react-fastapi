from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.database import Base 


class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer,primary_key=True,index = True)
    title = Column(String,index=True)
    session_id = Column(String,index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    nodes = relationship("StoryNode", back_populates="story")

class StoryNode(Base):
    __tablename__ = "story_nodes"

    id = Column(Integer,primary_key=True,index=True)
    story_id = Column(Integer, ForeignKey("stories.id"),index=True)
    content = Column(String)
    is_root = Column(Boolean, default=False)
    is_ending= Column(Boolean, default=False)
    is_winninng_endig = Column(Boolean,default=False)
    options = Column(JSON,default=list)

    story = relationship("story", back_populates="nodes")
    

