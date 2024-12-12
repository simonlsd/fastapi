from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from .models import Base


# Define Model
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    due_date = Column(Date, nullable=True)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  
    username = Column(String(50), unique=True, nullable=False)  
    password = Column(String(128), nullable=False)  
    email = Column(String(100), unique=True, nullable=False)