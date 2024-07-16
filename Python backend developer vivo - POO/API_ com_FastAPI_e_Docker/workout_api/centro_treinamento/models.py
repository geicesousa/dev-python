from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String

class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'atletas'
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(40), nullable=False)
    proprietario: Mapped['AtletaModel'] = relationship(back_populates='centro_treinamento')

    
    