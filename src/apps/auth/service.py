import datetime
from typing import Optional, Union, Dict, List

import ormar
from src.config.settings import metadata, database


class Category(ormar.Model):
    '''Categories by project
    '''

    class Meta:
        metadata = metadata
        database = database
    
    id: int = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=150)
    parent: Optional['Category'] = ormar.ForeignKey('Category', related_name='children', nullable=True)


class Toolkit(ormar.Model):
    '''
    Toolkit by project
    '''
    
    class Meta:
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=150)
    parent = ormar.ForeignKey('self', related_name='children', nullable=True)