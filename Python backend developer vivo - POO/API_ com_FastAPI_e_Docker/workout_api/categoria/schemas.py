from typing import Annotated
from pydantic import Field, UUID4
from workout_api.contrib.schemas import BaseSquema

class CategoriaIn(BaseSquema):
    nome: Annotated[str, Field(description='categoria', example='Scale', max_length=50)]

class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description='identificador da categoria')]
    