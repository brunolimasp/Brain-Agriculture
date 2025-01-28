import pytest
from src.models.tables import Property
from src.schemas.property import PropertyCreate


def test_create_valid_property(session):
    property_data = {
        "name": "Fazenda Boa Vista",
        "city": "Rio de Janeiro",
        "state": "RJ",
        "total_area": 100.0,
        "agricultural_area": 60.0,
        "vegetation_area": 40.0,
        "owner_id": 1,
    }
    new_property = Property(**property_data)
    session.add(new_property)
    session.commit()
    session.refresh(new_property)

    assert new_property.id is not None
    assert new_property.name == "Fazenda Boa Vista"


def test_invalid_property_area(session):
    property_data = {
        "name": "Fazenda Boa Vista",
        "city": "Rio de Janeiro",
        "state": "RJ",
        "total_area": 100.0,
        "agricultural_area": 80.0,
        "vegetation_area": 30.0,
        "owner_id": 1,
    }

    with pytest.raises(ValueError) as exc_info:
        PropertyCreate(**property_data)
    assert (
        "A soma das áreas agricultável e de vegetação não pode ultrapassar a área total da fazenda."
        in str(exc_info.value)
    )
