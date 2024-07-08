from db.models import LocationOrm
from db.session import async_session
from sqlalchemy import select

from .location_schemas import SLocation, SLocationAdd, SLocationId


class LocationRepository:
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
        async with async_session() as session:
            query = select(LocationOrm)
            result = await session.execute(query)
            location_models = result.scalars().all()
            location_schemas = [SLocation.model_validate(location_model) for location_model in location_models]
            return location_schemas
       
    # @classmethod
    # async def delete_all(cls) -> list[SLocation]:
    #     async with new_session() as session:
    #         query = select(LocationOrm)
    #         result = await session.execute(query)
    #         location_models = result.scalars().all()
    #         for location_model in location_models:
    #             await session.delete(location_model)
    #         await session.commit()
    #         location_schemas = [SLocation.model_validate(location_model) for location_model in location_models]
    #         return location_schemas
