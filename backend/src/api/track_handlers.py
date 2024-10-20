from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_async_session
from .track_manager import TrackRepository
from .track_schemas import STrackAdd, STrackId

track_router = APIRouter(
    prefix="/api/track",
    tags=["Маршруты"],
)


@track_router.post("", response_model=STrackId)
async def add_track(track: STrackAdd, db: AsyncSession = Depends(get_async_session)) -> STrackId:
    track_id = await TrackRepository.add_one_track(track)
    return STrackId(ok=True, track_id=track_id)
