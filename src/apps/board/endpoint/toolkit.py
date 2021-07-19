from typing import List
from fastapi import APIRouter, Depends, Body

from .. import schemas, service, models


toolkit_router = APIRouter()

@toolkit_router.post('/', response_model=schemas.OutToolkit)
async def create_toolkit(schema: schemas.CreateToolKit):
    return await models.Toolkit.objects.create(**schema.dict())

@toolkit_router.get('/', response_model=List[schemas.OutToolkit])
async def get_toolkit():
    return await models.Toolkit.objects.filter().all()
