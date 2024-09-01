from sqlalchemy import select
from sqlalchemy.orm import joinedload
from typing import List
from db.models import TrackOrm
from db.session import async_session_maker

from .track_schemas import STrack, STrackAdd


class TrackRepository:
    @classmethod
    async def _execute_query(cls, query):
        async with async_session_maker() as session:
            result = await session.execute(query)
            track_models = result.scalars().all()

            track_dicts = [track.__dict__ for track in track_models]
            for track_dict in track_dicts:
                track_dict.pop('_sa_instance_state', None)

            return track_models, track_dict
    

    @classmethod
    async def add_one_track(cls, data: STrackAdd) -> int:
        async with async_session_maker() as session:
            track_dict = data.model_dump()
            track = TrackOrm(**track_dict)
            session.add(track)
            await session.flush()
            await session.commit()
            return track.id
        
    @classmethod
    async def get_location_tracks(cls, location_id: int) -> list[STrack]:
        async with async_session_maker() as session:
            result = await session.execute(
                select(TrackOrm).filter_by(location_id=location_id)
            )
            tracks = result.scalars().all()
            track_schemas = [STrack.model_validate(track) for track in tracks]
            return track_schemas
