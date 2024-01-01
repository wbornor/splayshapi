from fastapi import APIRouter
from fastapi import HTTPException

from app.domain.items import ItemsDomain, ItemModel, NutType


class ItemsRouter:
    def __init__(self, items_domain: ItemsDomain) -> None:
        self.__items_domain = items_domain

    @property
    def router(self):
        api_router = APIRouter(prefix='/Prod/items', tags=['items'])

        @api_router.get('/', summary='List the latest items')
        def index_route() -> list[ItemModel]:
            return self.__items_domain.get_all_sorted()

        @api_router.get('/all', summary='List all the items sorted ascending')
        def get_all() -> list[ItemModel]:
            return self.__items_domain.get_all()

        @api_router.get('/nut/{nut_type}/all', summary='List the latest item by NutType')
        def get_by_nut_type(nut_type: str) -> list[ItemModel]:
            return self.__items_domain.get_by_nut_type_sorted(NutType.get_enum_by_name(nut_type))

        # @api_router.post('/create')
        # def create_recipe(items_model: ItemsModel):
        #     return self.__items_domain.create_recipe(items_model)

        @api_router.get('/get/{item_id}', summary='Fetch an item by id')
        def get_item(item_id: str) -> ItemModel:
            try:
                return self.__items_domain.get_item(item_id)
            except KeyError:
                raise HTTPException(status_code=400, detail='No item found')

        # @api_router.put('/update')
        # def update_recipe(items_model: ItemsModel):
        #     return self.__items_domain.update_recipe(items_model)
        #
        # @api_router.delete('/delete/{recipe_uid}')
        # def delete_recipe(recipe_uid: str):
        #     return self.__items_domain.delete_recipe(recipe_uid)
        #

        return api_router
