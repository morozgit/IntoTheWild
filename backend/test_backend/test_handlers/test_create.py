import pytest
from httpx import AsyncClient

from backend.src.api.location_handlers import SLocationAdd


@pytest.fixture
async def test_set_location(client: AsyncClient):
    test_location = SLocationAdd(
        name="Атлай",
        description="Жемчужина Сибири",
        image="Gorniy-Altay.png")
    response = client.post("/location", json=test_location.model_dump())
    assert response.status_code == 200
    data = response.json()
    assert data["ok"] == True
    assert "location_id" in data

@pytest.mark.asyncio
async def test_get_locations(client: AsyncClient):
    response = await client.get("/location/all_location")
    print(response.json())
    assert response.status_code == 200
