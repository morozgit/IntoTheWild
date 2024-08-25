import uvicorn
from fastapi import FastAPI
from src.admin import create_admin
from src.api.location_handlers import location_router
from src.admin import LocationAdmin, TrackAdmin
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(title="IntoTheWild")
app.include_router(location_router)
admin = create_admin(app)
admin.add_view(LocationAdmin)
admin.add_view(TrackAdmin)

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
