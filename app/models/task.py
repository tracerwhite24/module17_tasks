from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.backend.db import Base
from sqlalchemy.schema import CreateTable


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    slug = Column(String, unique=True, index=True)
    user = relationship("User", back_populates="tasks")

print(CreateTable(Task.__table__))

