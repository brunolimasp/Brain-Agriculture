from src.models.tables import Crop


def test_create_valid_crop(session):
    crop_data = {
        "name": "Soja",
        "harvest_year": 2023,
        "property_id": 1,
    }
    crop = Crop(**crop_data)
    session.add(crop)
    session.commit()
    session.refresh(crop)

    assert crop.id is not None
    assert crop.name == "Soja"
    assert crop.harvest_year == 2023
