import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

try:
    from models.tables import Producer, Property, Crop
except ImportError:
    pass


# Carrega as variáveis do arquivo .env
load_dotenv()

# Recupera as configurações do banco de dados a partir do .env
DATABASE_URL = (
    f"{os.getenv('DB_ENGINE')}://{os.getenv('DB_USERNAME')}:"
    f"{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST', 'localhost')}/"
    f"{os.getenv('DB_DATABASE')}"
)

# Cria o engine do banco de dados
engine = create_engine(DATABASE_URL)


def create_db_and_tables():
    """Cria as tabelas no banco de dados"""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Função usada como dependência no FastAPI para obter a sessão do banco."""
    with Session(engine) as session:
        yield session


if __name__ == "__main__":
    create_db_and_tables()
