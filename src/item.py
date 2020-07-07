# Item Class


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print('You have picked up the', self.name)

    def on_drop(self):
        print('You have dropped the', self.name)

    def isTreasure(self):
        return False


class LightSource(Item):
    pass


class Treasures(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

    def isTreasure(self):
        return True


class Weapons(Item):
    pass
