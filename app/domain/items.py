from uuid import uuid4
from pydantic import Field
from decimal import Decimal
from pydantic import BaseModel
from pydantic.types import UUID4
from typing import List, Optional

from app.repository.items import ItemsRepository


class ItemsModel(BaseModel):
    id: str = Field(..., example='talknut.6a05a9ba3f8c478bf79b57724023dd6afc9d06531317049cff83305fc3example')
    title: str = Field(..., example='@wbornor')
    content: str = Field(..., example='hello world')
    create_date: str = Field(..., example='2023-12-30 20:42:25')
    is_public: int = Field(..., example='1')
    nut_id: int = Field(..., example='1')
    nut_type: str = Field(..., example='TALKNUT')
    url: str = Field(..., example='https://twitter.com/wbornor/status/775853964348694528')


class ItemsDomain:
    def __init__(self, repository: ItemsRepository) -> None:
        self.__repository = repository

    def get_all(self):
        return self.__repository.get_all()

    def get_item(self, id: str):
        return self.__repository.get_item(id)

    # def create_item(self, item: ItemsModel):
    #     item.uid = str(uuid4())
    #     return self.__repository.create_item(item.dict())
    #
    # def update_item(self, item: ItemsModel):
    #     return self.__repository.update_item(item.dict())
    #
    # def delete_item(self, uid: str):
    #     return self.__repository.delete_item(uid)
