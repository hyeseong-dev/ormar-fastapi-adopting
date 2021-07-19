import datetime
from typing import Optional, Union, Dict, List

import ormar
from src.config.settings import metadata, database


class Category(ormar.Model):
    """ Categories by project
    """
    class Meta:
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=150)
    # parent: Optional['Category'] = ormar.ForeignKey(
    #     'Category', related_name="children", nullable=True
    # )


class Toolkit(ormar.Model):
    """ Toolkit by project
    """
    class Meta:
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=150)
    # parent = ormar.ForeignKey('self', related_name="children", nullable=True)


class Team(ormar.Model):
    class Meta:
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=150)


class ProjectTeam(ormar.Model):
    class Meta:
        tablename = "project_teams"
        database = database
        metadata = metadata


class Project(ormar.Model):
    """ Model project
    """
    class Meta:
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=150)
    description: str = ormar.Text()
    create_date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    categories: Optional[Union[Category, Dict]] = ormar.ForeignKey(
        Category, related_name="projects", name='category_id'
    )
    toolkits: Optional[Union[Toolkit, Dict]] = ormar.ForeignKey(
        Toolkit, related_name="projects", name='toolkit_id'
    )
    teams: Optional[Union[Team, List[Team]]] = ormar.ManyToMany(
        Team, related_name='projects',name='project_team_id', through=ProjectTeam
    )
