import uuid

class Item():
    def __init__(self, item_type):
        self.type = item_type
        self.uid = uuid.uuid4()

