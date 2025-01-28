import pytest
from src.models.tables import Producer


def test_create_valid_producer(session):
    producer_data = {"cpf": "78142771080", "cnpj": "", "name": "Produtor Teste"}
    producer = Producer(**producer_data)
    session.add(producer)
    session.commit()
    session.refresh(producer)

    assert producer.id is not None
    assert producer.name == "Produtor Teste"


def test_create_duplicate_producer(session):
    producer_data = {"cpf": "78142771080", "cnpj": "", "name": "Produtor Teste"}
    producer = Producer(**producer_data)
    session.add(producer)
    session.commit()

    # Tentativa de adicionar outro produtor com o mesmo CPF
    with pytest.raises(Exception):  # Espera erro devido à duplicidade
        duplicate_producer = Producer(**producer_data)
        session.add(duplicate_producer)
        session.commit()
