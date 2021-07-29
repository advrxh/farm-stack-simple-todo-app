import mongoengine
import datetime


class TodoItem(mongoengine.Document):
    description = mongoengine.StringField()
    status = mongoengine.StringField()
    created_at = mongoengine.DateTimeField(
        default=datetime.datetime.now())


class Status:
    pending = "pending"
    doing = "doing"
    complete = "complete"
