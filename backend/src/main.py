import uvicorn
from api.location.location_handlers import location_router
from fastapi import FastAPI

app = FastAPI(title="IntoTheWild")
app.include_router(location_router)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)