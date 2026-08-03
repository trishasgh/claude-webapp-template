"""SQLAlchemy engine, session factory, and declarative base."""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:////app/data/app.db")


class _Engine:
    engine = None
    SessionLocal = None


def _create_engine():
    connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
    _Engine.engine = create_engine(DATABASE_URL, connect_args=connect_args)
    _Engine.SessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=_Engine.engine
    )


_create_engine()

Base = declarative_base()


def get_db():
    db = _Engine.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    from app import models  # noqa: F401  (register models on Base)

    Base.metadata.create_all(bind=_Engine.engine)
