# Player Class


class Player:
    def __init__(self, name, current_room, list=[]):
        self.name = name
        self.current_room = current_room
        self.list = []

    def add_item(self, item):
        self.list.append(item)

    def remove_item(self, item):
        self.list.remove(item)
