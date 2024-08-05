from sqlalchemy import select

from db.models import LocationOrm
from db.session import async_session

from .location_schemas import SLocation, SLocationAdd, SLocationId


class LocationRepository:
    @classmethod
    async def _execute_query(cls, query):
        async with async_session() as session:
            result = await session.execute(query)
            location_models = result.scalars().all()

            location_dicts = [loc.__dict__ for loc in location_models]
            for loc_dict in location_dicts:
                loc_dict.pop('_sa_instance_state', None)

            return location_models, location_dicts

    @classmethod
    async def add_one_location(cls, data: SLocationAdd) -> int:
        async with async_session() as session:
            location_dict = data.model_dump()
            print('location_dict', location_dict)
            location = LocationOrm(**location_dict)
            session.add(location)
            await session.flush()
            await session.commit()
            return location.id

    @classmethod
    async def find_all(cls) -> list[SLocation]:
        query = select(LocationOrm)
        location_models, location_dicts = await cls._execute_query(query)
        location_schemas = [SLocation.model_validate(loc_dict) for loc_dict in location_dicts]
        return location_schemas

    @classmethod
    async def delete_all(cls) -> list[SLocation]:
        query = select(LocationOrm)
        location_models, location_dicts = await cls._execute_query(query)
        
        async with async_session() as session:
            for location_model in location_models:
                await session.delete(location_model)
            await session.commit()

        location_schemas = [SLocation.model_validate(loc_dict) for loc_dict in location_dicts]
        return location_schemas
