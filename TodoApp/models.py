import datetime
from database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    