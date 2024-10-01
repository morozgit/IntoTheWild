import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_set_location(ac: AsyncClient):
    print(f"ac in test is instance of {type(ac)}")
    test_location = {
        "name": "Атлай",
        "description": "Жемчужина Сибири",
        "image": "Gorniy-Altay.png"
    }
    response = await ac.post("/api/location", json=test_location)
    assert response.status_code == 200
    data = response.json()
    print('data', data)
    assert data["ok"] is True
    assert "location_id" in data


@pytest.mark.asyncio
async def test_get_locations(ac: AsyncClient):
    response = await ac.get("/api/location/all_location")
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert isinstance(data, list)
    if data:
        assert "name" in data[0]
        assert "description" in data[0]
        assert "image" in data[0]
