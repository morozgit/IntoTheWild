from pydantic import BaseModel, Field


class SLocationAdd(BaseModel):
    name: str = Field(..., description='Название локации')
    description: str = Field(..., description='Краткое описание локации')
    image: str = Field(..., description='Изображение локации')


class SLocation(SLocationAdd):
    id: int

    class ConfigDict:
        from_attributes = True


class SLocationId(BaseModel):
    ok: bool = True
    location_id: int