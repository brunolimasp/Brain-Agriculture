# src/routers/crop.py
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from ..database import engine
from ..models.tables import Crop
from ..schemas.crop import CropCreate, CropRead

router = APIRouter(prefix="/crops", tags=["Crops"])


def get_session():
    with Session(engine) as session:
        yield session


@router.post("/register", response_model=CropRead)
def create_crop(crop: CropCreate, session: Session = Depends(get_session)):
    # Cria e salva a nova safra
    new_crop = Crop(**crop.dict())
    session.add(new_crop)
    session.commit()
    session.refresh(new_crop)
    return new_crop


@router.get("/list", response_model=list[CropRead])
def list_crops(session: Session = Depends(get_session)):
    # Lista todas as safras
    statement = select(Crop)
    crops = session.exec(statement).all()
    return crops
