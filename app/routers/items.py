from fastapi import APIRouter
from fastapi import HTTPException

from app.domain.items import ItemsDomain, ItemsModel


class ItemsRouter:
    def __init__(self, items_domain: ItemsDomain) -> None:
        self.__items_domain = items_domain

    @property
    def router(self):
        api_router = APIRouter(prefix='/items', tags=['items'])

        @api_router.get('/')
        def index_route():
            return 'Hello! Welcome to items index route'

        @api_router.get('/all')
        def get_all():
            return self.__items_domain.get_all()

        # @api_router.post('/create')
        # def create_recipe(items_model: ItemsModel):
        #     return self.__items_domain.create_recipe(items_model)

        @api_router.get('/get/{item_id}')
        def get_item(item_id: str):
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
