# src/routers/property.py
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from ..database import engine
from ..models.tables import Property
from ..schemas.property import PropertyCreate, PropertyRead

router = APIRouter(prefix="/properties", tags=["Properties"])


def get_session():
    with Session(engine) as session:
        yield session


@router.post("/register", response_model=PropertyRead)
def create_property(property: PropertyCreate, session: Session = Depends(get_session)):
    # Cria e salva a nova propriedade
    new_property = Property(**property.dict())
    session.add(new_property)
    session.commit()
    session.refresh(new_property)
    return new_property


@router.get("/list", response_model=list[PropertyRead])
def list_properties(session: Session = Depends(get_session)):
    # Lista todas as propriedades
    statement = select(Property)
    properties = session.exec(statement).all()
    return properties
