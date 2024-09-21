from db.session import get_async_session
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .location_manager import LocationRepository
from .location_schemas import SLocation, SLocationAdd, SLocationId
from .track_manager import TrackRepository

location_router = APIRouter(
    prefix="/api/location",
    tags=["Локации"],
)


@location_router.post("", response_model=SLocationId)
async def add_location(location: SLocationAdd, db: AsyncSession = Depends(get_async_session)) -> SLocationId:
    location_id = await LocationRepository.add_one_location(location)
    return SLocationId(ok=True, location_id=location_id)


@location_router.get("/all_location")
async def get_locations() -> list[SLocation]:
    locations = await LocationRepository.find_all()
    return locations


@location_router.get("/{location_id}")
async def get_location(location_id: int):
    tracks = await TrackRepository.get_location_tracks(location_id)
    return tracks


@location_router.post("/delete_all_locations")
async def delete_all_location() -> list[SLocation]:
    locations = await LocationRepository.delete_all()
    return locations
