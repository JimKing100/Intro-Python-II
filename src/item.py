# Item Class


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print('You have picked up the', self.name)

    def on_drop(self):
        print('You have dropped the', self.name)