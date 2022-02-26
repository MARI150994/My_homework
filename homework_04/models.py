import os
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:password@localhost/test_async_db"

engine = create_async_engine(PG_CONN_URI, echo=True)
Base = declarative_base(bind=engine)
Session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="posts")