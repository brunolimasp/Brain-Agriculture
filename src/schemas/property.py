from pydantic import BaseModel, Field, model_validator, ConfigDict
from src.schemas.producer import ProducerRead


class PropertyBase(BaseModel):
    name: str = Field(..., max_length=255, description="Nome da fazenda")
    city: str = Field(..., max_length=100, description="Cidade da fazenda")
    state: str = Field(..., max_length=2, description="Sigla do estado")
    total_area: float = Field(..., description="Área total da fazenda em hectares")
    agricultural_area: float = Field(..., description="Área agricultável em hectares")
    vegetation_area: float = Field(..., description="Área de vegetação em hectares")

    model_config = ConfigDict(arbitrary_types_allowed=True)


class PropertyCreate(PropertyBase):
    owner_id: int

    @model_validator(mode="after")
    def validate_areas(cls, values):
        total_area = values.total_area
        agricultural_area = values.agricultural_area
        vegetation_area = values.vegetation_area

        if agricultural_area + vegetation_area > total_area:
            raise ValueError(
                "A soma das áreas agricultável e de vegetação não pode ultrapassar a área total da fazenda."
            )
        return values


class PropertyRead(PropertyBase):
    id: int
    owner: ProducerRead

    class Config:
        from_attributes = True
