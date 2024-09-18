from sqladmin import Admin, ModelView
from db.session import engine
from fastapi import FastAPI
from db.models import LocationOrm, TrackOrm


def create_admin(app: FastAPI):
    return Admin(app, engine)


class LocationAdmin(ModelView, model=LocationOrm):
    column_list = ["id", "name", "description", "image"]


class TrackAdmin(ModelView, model=TrackOrm):
    column_list = ["id", "name", "description", "image", "created_at", "updated_at", "location_id"]
