import uvicorn
from fastapi import FastAPI
from src.admin import create_admin
from src.api.location_handlers import location_router
from src.admin import LocationAdmin, TrackAdmin


app = FastAPI(title="IntoTheWild")
app.include_router(location_router)
admin = create_admin(app)
admin.add_view(LocationAdmin)
admin.add_view(TrackAdmin)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
