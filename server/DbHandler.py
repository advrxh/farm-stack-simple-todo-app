import mongoengine
import pymongo
from DbModels import *
import json
import datetime


class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime):
            return (str(z))
        else:
            return super().default(z)


class Handler:

    def __init__(self, db) -> None:

        self.conn = mongoengine.connect(db)

    def addItem(self, description):
        _item = TodoItem(
            description=description,
            status=Status.pending
        )

        _item.save()

        return str(_item.id)

    def deleteItem(self, _id):
        TodoItem.objects(id=_id).delete()

        return True

    def update(self, status: str = "pending", _id: str = None, desc: str = None):

        try:

            TodoItem.objects(id=_id).update(
                status=status,
                description=desc
            )

            return True
        except Exception as e:
            return False

    def getItems(self):

        _items = TodoItem.objects().all()

        _lst = []

        for item in _items:
            item = dict(item.to_mongo())
            item["_id"] = str(item["_id"])
            item = json.loads(json.dumps(item, cls=DateTimeEncoder))
            _lst.append(item)

        return _lst

    def getItem(self, _id):

        _item = TodoItem.objects(id=_id).first()

        _item = dict(_item.to_mongo())
        _item["_id"] = str(_item["_id"])
        _item = json.loads(json.dumps(_item, cls=DateTimeEncoder))

        return _item


if __name__ == "__main__":
    n = Handler("todo-app")

    n.updateDescription(description="lmao", _id="6102bbebaf5457b823528889")
