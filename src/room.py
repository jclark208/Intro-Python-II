# Implement a class to hold room information. This should have name and
# description attributes.
class Rooms:
    def __init__(self,name,description,n_to=None,s_to=None,e_to=None,w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.loot = []
    def __str__(self):
        return f'This is the {self.name}. Description: {self.description} Holy crap there are a few items in here: {self.loot}'
        
    def remove_item(self, item):
        self.loot.remove(item)

    def add_item(self, item):
        self.loot.append(item)