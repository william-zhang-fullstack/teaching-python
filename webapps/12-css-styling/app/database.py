class ShoppingList:
    def __init__(self):
        self.records = dict()
        self.next_id = 0

    def getall(self):
        return self.records.values()

    def get(self, uid):
        return self.records[uid]

    def create(self, name, quantity):
        self.records[self.next_id] = {
            'uid': self.next_id,
            'name': name,
            'quantity': quantity
        }
        self.next_id += 1

    def delete(self, uid):
        del self.records[uid]

    def update(self, uid, name, quantity):
        self.records[uid]['name'] = name
        self.records[uid]['quantity'] = quantity
