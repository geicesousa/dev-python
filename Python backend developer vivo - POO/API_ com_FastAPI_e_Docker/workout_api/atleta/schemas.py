''' responsável por fazer validações e serializar os dados, pela exibição dos dados '''
from typing import Annotated, Optional
from pydantic import Field, PositiveFloat
from workout_api.categoria.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from workout_api.contrib.schemas import BaseSquema, OutMixin

class Atleta(BaseSquema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Geice', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678901', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=27)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example='65.6', max_length=50)]
    altura: Annotated[PositiveFloat, Field(description='do atleta', example=1.65)]
    sexo: Annotated[str, Field(description='do atleta', example='F', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='CT do atleta')]

class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSquema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='Geice', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', example=27, max_length=3)]