# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine

from app import app  # Importe seu app do FastAPI
from src.database import get_session  # Função que você usa como Depends para a sessão


@pytest.fixture(name="test_engine")
def fixture_test_engine():
    # Cria um banco de dados SQLite em memória para testes
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    return engine


@pytest.fixture(name="session")
def fixture_session(test_engine):
    with Session(test_engine) as session:
        yield session


@pytest.fixture(name="client")
def fixture_client(session):
    """
    Retorna um TestClient que utiliza a sessão de teste.
    Isso permite que a aplicação utilize o banco em memória.
    """

    # Override da dependência get_session para usar nossa session de teste
    def override_get_session():
        yield session

    app.dependency_overrides[get_session] = override_get_session

    with TestClient(app) as client:
        yield client

    # Remove o override após os testes
    app.dependency_overrides.clear()
