import uuid
from datetime import datetime

class Tree:

    def __init__(self):
        self.home = str(uuid.uuid4())
        self.root = Store(id=self.home, tags=None, date=str(datetime.now()), parent=None)
        self.trace = {self.home: self.root}
        self.active = self.home

    def add(self, tags=None):
        this_uuid = str(uuid.uuid4())
        this_node = Store(id=this_uuid, tags=tags, date=str(datetime.now()), parent=self.active)
        self.trace[this_uuid] = this_node
        self.active = this_uuid

    def display_current(self):
        for key in self.trace[self.active].data_store:
            print('{}: {}'.format(key, self.trace[self.active].data_store[key]))

    def get_history(self):
        parent = self.trace[self.active].data_store['parent']
        i = 0
        while parent:
            print('Step {}:\t{}'.format(i, parent))
            parent = self.trace[parent].data_store['parent']
            i -= 1



class Store:

    def __init__(self, **kwargs):
        self.data_store = kwargs