class Item():

    number_of_items =  0

    # Create an item
    def __init__ (self, item_name):
        self.name = item_name
        self.description = None
        Item.number_of_items = Item.number_of_items + 1

    # Set description for this item
    def set_description(self, item_description):
        self.description = item_description

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    # display item description
    def describe(self):
        print( "You can see a " + self.name + ". ") 
        print(self.description) 

# Creating a potion subclass
class Potion(Item):
    def __init__(self, item_name):
        super().__init__(item_name)
        self.status = None
        self.effect = None

    # Set the attributes of this Item
    def set_effect(self, affected_status, effect):
        self.status = affected_status
        self.effect = effect

# Creating a weapon subclass
class Weapon(Item):
    def ___init__(self, item_name):
        super().__init__(item_name)
        self.attack = None
        self.wear = None

    # Set the atributes
    def set_attributes(self, attack_points, weapon_wear):
        self.attack = attack_points
        self.weapon = weapon_wear
