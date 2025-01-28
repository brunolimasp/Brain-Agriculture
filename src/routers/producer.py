from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from ..database import engine
from ..models.tables import Producer
from ..schemas.producer import ProducerCreate, ProducerRead

router = APIRouter(prefix="/producers", tags=["Producers"])


def get_session():
    with Session(engine) as session:
        yield session


@router.post("/register", response_model=ProducerRead)
def create_producer(producer: ProducerCreate, session: Session = Depends(get_session)):
    # Validação: CPF ou CNPJ deve ser preenchido, mas não ambos
    if not producer.cpf and not producer.cnpj:
        raise HTTPException(
            status_code=400, detail="É necessário preencher CPF ou CNPJ."
        )
    if producer.cpf and producer.cnpj:
        raise HTTPException(
            status_code=400, detail="Preencha apenas um campo: CPF ou CNPJ, não ambos."
        )

    # Verifica se o CPF ou CNPJ já existe
    existing_producer = (
        session.query(Producer)
        .filter((Producer.cpf == producer.cpf) | (Producer.cnpj == producer.cnpj))
        .first()
    )
    if existing_producer:
        raise HTTPException(
            status_code=400, detail="Já existe um produtor com esse CPF ou CNPJ."
        )

    # Cria e salva o novo produtor
    new_producer = Producer(**producer.model_dump())
    session.add(new_producer)
    session.commit()
    session.refresh(new_producer)
    return new_producer


@router.delete("/delete/{producer_id}", response_model=ProducerRead)
def delete_producer(producer_id: int, session: Session = Depends(get_session)):
    # Busca o produtor pelo ID
    statement = select(Producer).where(
        Producer.id == producer_id, Producer.is_deleted == False
    )
    producer = session.exec(statement).first()

    if not producer:
        raise HTTPException(
            status_code=404, detail="Produtor não encontrado ou já deletado."
        )

    # Marca como deletado (soft delete)
    producer.is_deleted = True
    session.add(producer)
    session.commit()
    session.refresh(producer)

    return producer
