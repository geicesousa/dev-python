from uuid import uuid4
from fastapi import APIRouter, status, Body, HTTPException
from workout_api.categoria.schemas import CategoriaIn, CategoriaOut
from workout_api.categoria.models import CategoriaModel
from workout_api.contrib.dependencies import DatabaseDependency

from sqlalchemy.future import select
from pydantic import UUID4

router = APIRouter()
@router.post(
    path='/', 
    summary='Criar nova categoria',
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut
)
async def post(
    db_session: DatabaseDependency, 
    categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut:    
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())
    
    db_session.add(categoria_model)
    await db_session.commit()
    breakpoint()
    
    return categoria_out

@router.get(
    '/', 
    summary='Consultar todas as categorias',
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaOut],
)
async def query(
   db_session: DatabaseDependency
) -> list[CategoriaOut]: 
   categorias: list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()
#   breakpoint()
   return categorias


@router.get(
    '/{id}', 
    summary='Consultar uma categoria por id',
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut
)
async def get(id: UUID4, db_session: DatabaseDependency) -> CategoriaOut: 
    categoria: CategoriaOut = (
      await db_session.execute(select(CategoriaModel).filter_by(id=id))
    ).scalars().first()
   # breakpoint()

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'categoria não encontrada no id {id}'
        )
    
    return categoria
