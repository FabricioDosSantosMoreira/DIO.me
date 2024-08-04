from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.contrib.models import BaseModel


class CategoriaModel(BaseModel):
    __tablename__: str = "categorias"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)

    atleta: Mapped['AtletaModel'] = relationship(back_populates='categoria')
