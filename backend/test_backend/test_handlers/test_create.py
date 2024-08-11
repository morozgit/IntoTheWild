import pytest
from httpx import AsyncClient

from backend.src.api.location_handlers import SLocationAdd


async def test_set_location(ac: AsyncClient):
    test_location = SLocationAdd(
        name="Атлай",
        description="Жемчужина Сибири",
        image="Gorniy-Altay.png")
    response = await ac.post("/location", json=test_location.model_dump())
    assert response.status_code == 200
    data = response.json()
    print('data', data)
    assert data["ok"] == True
    assert "location_id" in data


async def test_get_locations(ac: AsyncClient):
    response = await ac.get("/location/all_location")
    print(response.json())
    assert response.status_code == 200

