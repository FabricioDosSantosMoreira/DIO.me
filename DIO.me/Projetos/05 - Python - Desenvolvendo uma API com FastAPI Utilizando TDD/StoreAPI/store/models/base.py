from datetime import datetime
from decimal import Decimal
from typing import Annotated, Any, Dict
from uuid import uuid4

from bson import Decimal128
from pydantic import UUID4, BaseModel, Field, model_serializer

from store.core.config import settings


class CreateBaseModel(BaseModel):

    id: Annotated[UUID4, Field(
        default_factory=lambda: uuid4(), 
        description="Product Identifier", 
        examples=uuid4()
    )]
    
    created_at: Annotated[datetime, Field(
        default_factory=lambda: datetime.now(settings.UTC_TIMEZONE),
        description="Product creation date",
        examples=datetime.now(settings.UTC_TIMEZONE)
    )]

    updated_at: Annotated[datetime, Field(
        default_factory=lambda: datetime.now(settings.UTC_TIMEZONE),
        description="Product update date",
        examples=datetime.now(settings.UTC_TIMEZONE)
        )]

    @model_serializer
    def set_model(self) -> Dict[str, Any]:
        self_dict = dict(self)

        for key, value in self_dict.items():
            if isinstance(value, Decimal):
                self_dict[key] = Decimal128(str(value))

        return self_dict
    

class UpdateBaseModel(BaseModel):

    updated_at: Annotated[datetime, Field(
        default_factory=lambda: datetime.now(settings.UTC_TIMEZONE),
        description="Product update date",
        examples=datetime.now(settings.UTC_TIMEZONE)
        )]

    @model_serializer
    def set_model(self) -> Dict[str, Any]:
        self_dict = dict(self)

        for key, value in self_dict.items():
            if isinstance(value, Decimal):
                self_dict[key] = Decimal128(str(value))

        return self_dict
