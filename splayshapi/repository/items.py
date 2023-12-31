from boto3.dynamodb.conditions import Attr
from botocore.exceptions import ClientError
from boto3.resources.base import ServiceResource
from boto3.dynamodb.conditions import Key, Attr

from splayshapi.domain.nuttype import NutType


class ItemsRepository:

    def __init__(self, db: ServiceResource) -> None:
        self.__db = db  # db resource will be injected when this repository is created in the app.py
        self.__TABLE_ITEM_NAME = 'splayshdb.dev.items'  # todo: dynamic env
        self.__INDEX_ITEM_ISPUBLIC_CREATEDATE_NAME = 'item-ispublic-createdate'
        self.__INDEX_ITEM_NUT_CREATEDATE_NAME = 'item-nut-createdate'

    def get_all(self):
        table = self.__db.Table(self.__TABLE_ITEM_NAME)
        response = table.scan(FilterExpression=Attr('is_public').eq(1))
        return response.get('Items', [])

    def get_item(self, id: str):
        try:
            table = self.__db.Table(self.__TABLE_ITEM_NAME)
            response = table.get_item(Key={'id': id})
            return response['Item']
        except ClientError as e:
            raise ValueError(e.response['Error']['Message'])

    def get_all_sorted(self):
        try:
            table = self.__db.Table(self.__TABLE_ITEM_NAME)
            response = table.query(IndexName=self.__INDEX_ITEM_ISPUBLIC_CREATEDATE_NAME,
                                   KeyConditionExpression=Key('is_public').eq(1),
                                   ScanIndexForward=False
                                   )
            return response['Items']
        except ClientError as e:
            raise ValueError(e.response['Error']['Message'])

    def get_by_nut_type_sorted(self, nut_type: NutType):
        try:
            table = self.__db.Table(self.__TABLE_ITEM_NAME)
            response = table.query(IndexName=self.__INDEX_ITEM_NUT_CREATEDATE_NAME,
                                   KeyConditionExpression=Key('nut_type').eq(nut_type.name),
                                   ScanIndexForward=False
                                   )
            return response['Items']
        except ClientError as e:
            raise ValueError(e.response['Error']['Message'])

    # def create_item(self, item: dict):
    #     table = self.__db.Table(self.__TABLE_ITEM_NAME)
    #     response = table.put_item(Item=item)
    #     return response

    # def update_item(self, item: dict):
    #     table = self.__db.Table(self.__TABLE_ITEM_NAME)
    #     response = table.update_item(
    #         Key={'uid': item.get('uid')},
    #         UpdateExpression="""
    #             set
    #                 author=:author,
    #                 description=:description,
    #                 ingredients=:ingredients,
    #                 title=:title,
    #                 steps=:steps
    #         """,
    #         ExpressionAttributeValues={
    #             ':author': item.get('author'),
    #             ':description': item.get('description'),
    #             ':ingredients': item.get('ingredients'),
    #             ':title': item.get('title'),
    #             ':steps': item.get('steps')
    #         },
    #         ReturnValues="UPDATED_NEW"
    #     )
    #     return response

    # def delete_item(self, uid: str):
    #     table = self.__db.Table(self.__TABLE_ITEM_NAME)
    #     response = table.delete_item(
    #         Key={'uid': uid}
    #     )
    #     return response
