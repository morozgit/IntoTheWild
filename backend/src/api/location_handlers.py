import boto3
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_async_session
from .location_manager import LocationRepository
from .location_schemas import SLocation, SLocationAdd, SLocationId
from .track_manager import TrackRepository

location_router = APIRouter(
    prefix="/location",
    tags=["Локации"],
)

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)

@location_router.post("", response_model=SLocationId)
async def add_location(location: SLocationAdd, db: AsyncSession = Depends(get_async_session)) -> SLocationId:
    location_id = await LocationRepository.add_one_location(location)
    return SLocationId(ok=True, location_id=location_id)


@location_router.get("/all_location")
async def get_locations() -> list[SLocation]:
    locations = await LocationRepository.find_all()
    return locations

@location_router.get("/images")
def get_images():
    bucket_name = 'into-the-wild-images'
    base_url = f'https://storage.yandexcloud.net/{bucket_name}/'
    
    images = []
    for key in s3.list_objects(Bucket=bucket_name)['Contents']:
        image_url = base_url + key['Key']
        images.append(image_url)
    print('images', images)
    return images


@location_router.get("/{location_id}")
async def get_location(location_id: int):
    tracks = await TrackRepository.get_location_tracks(location_id)
    return tracks


@location_router.post("/delete_all_locations")
async def delete_all_location() -> list[SLocation]:
    locations = await LocationRepository.delete_all()
    return locations
