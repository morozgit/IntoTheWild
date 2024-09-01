from pydantic import BaseModel, Field


class STrackAdd(BaseModel):
    name: str = Field(..., description='Название маршрута')
    description: str = Field(..., description='Описание маршрута')
    image: str = Field(..., description='Изображение маршрута')
    location_id: int = Field(..., description='Локация')


class STrack(STrackAdd):
    id: int

    class Config:
        from_attributes = True


class STrackId(BaseModel):
    ok: bool = True
    track_id: int
