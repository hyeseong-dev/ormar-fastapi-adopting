from typing import List

from fastapi import APIRouter, Depends
from .. import schemas, service, models


category_router = APIRouter()


@category_router.post('/', response_model=schemas.OutCategory)
async def create_category(schema: schemas.CreateCategory):
    """ Create category of project """
    return await models.Category.objects.create(**schema.dict())
    # return await service.category_s.create(schema)


@category_router.get('/', response_model=List[schemas.OutCategory])
async def get_all_categories():
    return await models.Category.objects.filter().all()