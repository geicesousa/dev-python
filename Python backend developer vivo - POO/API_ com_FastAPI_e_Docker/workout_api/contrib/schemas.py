from typing import Annotated
from pydantic import BaseModel, UUID4, Field
from datetime import datetime

class BaseSquema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes = True


class OutMixin(BaseSquema):
    id: Annotated[UUID4, Field(description='identificador')]
    created_at: Annotated[datetime, Field(description='data de criação')]