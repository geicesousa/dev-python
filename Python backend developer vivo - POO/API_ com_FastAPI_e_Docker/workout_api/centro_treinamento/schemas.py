from typing import Annotated
from pydantic import Field, UUID4
from workout_api.contrib.schemas import BaseSquema

class CentroTreinamentoIn(BaseSquema):
    nome: Annotated[str, Field(description='Nome do CT', example='Geice', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do CT', example='Rua Abelardo, 154, Esmero', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do CT', example='Fulano', max_length=40)]


class CentroTreinamentoAtleta(BaseSquema):
    nome: Annotated[str, Field(description='Nome do CT', example='Geice', max_length=20)]


class CentroTreinamentoOut(BaseSquema):
   id: Annotated[UUID4, Field(description='Identificador de centro de treinamento')]
   