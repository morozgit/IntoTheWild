import datetime
from typing import Annotated, List

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=text("TIMEZONE('utc', now())"),
)]


class Base(DeclarativeBase):
    pass


class LocationOrm(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]
    image: Mapped[str | None]
    track: Mapped[List["TrackOrm"]] = relationship(
        back_populates="location",
    )

    def __repr__(self):
        return f"<LocationOrm(id={self.id}, name={self.name})>"


class TrackOrm(Base):
    __tablename__ = "tracks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]
    image: Mapped[str | None]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    location_id: Mapped[int] = mapped_column(ForeignKey("locations.id", ondelete="CASCADE"))
    location: Mapped["LocationOrm"] = relationship(
        back_populates="track",
    )

    def __repr__(self):
        return f"<TrackOrm(id={self.id}, name={self.name}, location_id={self.location_id})>"
