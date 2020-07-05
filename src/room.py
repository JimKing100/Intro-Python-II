# Room Class


class Room:
    def __init__(self, name, description, list=[], n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.list = []
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def add_item(self, item):
        self.list.append(item)

    def remove_item(self, item):
        self.list.remove(item)
