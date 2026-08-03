"""Public page/meta endpoints."""
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app import schemas
from app.database import get_db
from app.models import Visit

router = APIRouter(tags=["meta"])


@router.get("/api/health")
def health():
    return {"status": "ok"}


@router.get("/api/visits", response_model=list[schemas.VisitOut])
def visits(request: Request, db: Session = Depends(get_db)):
    db.add(Visit(path=request.url.path))
    db.commit()
    recent = db.query(Visit).order_by(Visit.visited_at.desc()).limit(20).all()
    return recent
