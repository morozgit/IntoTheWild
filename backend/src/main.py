import uvicorn
from fastapi import FastAPI
from src.admin import create_admin
from src.api.location_handlers import location_router
from src.api.track_handlers import track_router

from src.admin import LocationAdmin, TrackAdmin
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="IntoTheWild")
app.include_router(location_router)
app.include_router(track_router)
admin = create_admin(app)
admin.add_view(LocationAdmin)
admin.add_view(TrackAdmin)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://31.129.44.137",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
