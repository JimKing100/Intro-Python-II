# Player Class


class Player:
    def __init__(self, name, current_room, list=[], score=0):
        self.name = name
        self.current_room = current_room
        self.list = []
        self.score = score

    def add_item(self, item):
        self.list.append(item)
        if item.isTreasure() is True:
            self.score = self.score + item.value

    def remove_item(self, item):
        self.list.remove(item)
        if item.isTreasure() is True:
            self.score = self.score - item.value
