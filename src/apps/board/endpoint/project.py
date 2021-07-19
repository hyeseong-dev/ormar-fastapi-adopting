from typing import List
from fastapi import APIRouter, Depends, Body

from .. import schemas, service, models


project_router = APIRouter()


@project_router.post('/', response_model=models.Project)
async def create_project(schema: schemas.CreateProject, repo_name: str = Body(...)):
    proj = models.Project(**schema.dict(exclude={'team'}))
    await proj.save()
    team = await models.Team.objects.get(pk=schema.dict().pop('team')[0])
    await proj.team.add(team)
    return proj


@project_router.get('/', response_model=List[models.Project])
async def get_all_projects():
    return await models.Project.objects.select_related(['category', 'toolkit', 'team']).all()


@project_router.post('/team', response_model=models.Team)
async def create_team(schema: models.Team):
    return await schema.save()


@project_router.get('/team', response_model=List[models.Team])
async def get_all_teams():
    return await models.Team.objects.all()