from pydantic import BaseModel, Field, ConfigDict
from src.schemas.property import PropertyRead


class CropBase(BaseModel):
    name: str = Field(..., max_length=100, description="Nome da cultura")
    harvest_year: int = Field(..., description="Ano da safra")

    model_config = ConfigDict(arbitrary_types_allowed=True)


class CropCreate(CropBase):
    property_id: int


class CropRead(CropBase):
    id: int
    property: PropertyRead

    class Config:
        from_attributes = True
