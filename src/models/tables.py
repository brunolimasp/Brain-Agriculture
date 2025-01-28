from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


# produtor
class Producer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cpf: str = Field(unique=True, index=True, max_length=11)
    cnpj: str = Field(unique=True, index=True, max_length=14)
    name: str = Field(max_length=255)
    is_deleted: bool = Field(default=False)
    properties: List["Property"] = Relationship(back_populates="owner")


# propriedade - Fazenda
class Property(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    city: str = Field(max_length=100)
    state: str = Field(max_length=2)  # Sigla do estado (ex.: SP, RJ)
    total_area: float  # Área total da fazenda (em hectares)
    agricultural_area: float  # Área agricultável
    vegetation_area: float  # Área de vegetação
    owner_id: int = Field(foreign_key="producer.id")
    owner: Producer = Relationship(back_populates="properties")
    crops: List["Crop"] = Relationship(back_populates="property")


# safra-colheita
class Crop(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)  # Nome da cultura (ex.: Soja, Milho)
    harvest_year: int  # Ano da safra (ex.: 2021, 2022)
    property_id: int = Field(foreign_key="property.id")
    property: Property = Relationship(back_populates="crops")
