import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.admin import LocationAdmin, TrackAdmin, create_admin
from src.api.location_handlers import location_router
from src.api.track_handlers import track_router

app = FastAPI(title="IntoTheWild")
app.include_router(location_router)
app.include_router(track_router)
admin = create_admin(app)
admin.add_view(LocationAdmin)
admin.add_view(TrackAdmin)

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://31.129.44.137"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
