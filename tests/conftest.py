import pytest
from sqlmodel import SQLModel, Session, create_engine


from src.models.tables import Producer, Property, Crop


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