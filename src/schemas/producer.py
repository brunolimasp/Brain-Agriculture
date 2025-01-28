from typing import Optional
from pydantic import BaseModel, Field, field_validator, ConfigDict, model_validator
from validate_docbr import CPF, CNPJ


class ProducerBase(BaseModel):
    cpf: Optional[str] = Field(None, max_length=11, description="CPF do produtor")
    cnpj: Optional[str] = Field(None, max_length=14, description="CNPJ do produtor")
    name: str = Field(..., max_length=255, description="Nome do produtor")

    # Substitui a class Config do Pydantic v1
    model_config = ConfigDict(arbitrary_types_allowed=True)

    # Validação individual de CPF (se houver valor)
    @field_validator("cpf")
    def validar_cpf(cls, value):
        # Se for None ou string vazia, não valida
        if not value:
            return value

        doc = CPF()
        if not doc.validate(value):
            raise ValueError("CPF inválido.")
        return value

    # Validação individual de CNPJ (se houver valor)
    @field_validator("cnpj")
    def validar_cnpj(cls, value):
        # Se for None ou string vazia, não valida
        if not value:
            return value

        doc = CNPJ()
        if not doc.validate(value):
            raise ValueError("CNPJ inválido.")
        return value

    # Validação final: exige que exatamente um campo seja preenchido
    @model_validator(mode="after")
    def check_cpf_cnpj(cls, values):
        cpf = values.cpf
        cnpj = values.cnpj

        if not cpf and not cnpj:
            raise ValueError("É necessário informar CPF ou CNPJ.")
        if cpf and cnpj:
            raise ValueError("Informe apenas CPF ou apenas CNPJ, não ambos.")

        return values


class ProducerCreate(ProducerBase):
    pass


class ProducerRead(ProducerBase):
    id: int

    # Exemplo: Modo de compatibilidade para extrair atributos de ORM
    class Config:
        from_attributes = True
