"""Pydantic request/response models."""
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class VisitOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    path: str
    visited_at: datetime
