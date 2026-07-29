class Inventory():
    def __init__(self):
        self.items = []
    def _add_to_inventory(self, item):
        self.items.append(item)
    def _get_items(self):
        return self.items
    def _get_items_counted(self):
        items_counted = {}
        for item in self.items:
            if items_counted.get(item) == None:
                items_counted[item] = 1
            else:
                items_counted[item] += 1
        return items_counted

    def _set_items(self,items):
        self.items = items
