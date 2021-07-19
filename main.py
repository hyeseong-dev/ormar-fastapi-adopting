from fastapi import FastAPI

from src.apps import routers
from src.config.settings import database, engine, metadata


app = FastAPI()

metadata.create_all(engine)
app.state.database = database

app.include_router(routers.api_router)

@app.on_event('startup')
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event('shutdown')
async def shutdown() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.disconnect()