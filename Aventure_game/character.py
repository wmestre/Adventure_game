class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

# creating an enemy subclass 
class Enemy(Character): #Putting Character inside the brackets tells Python that the Enemy class will inherit all of the methods from Character.
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    # set the weakness of this character
    def set_weakness(self, enemy_weakness):
        self.weakness = enemy_weakness
    
    # output the enemy weakness
    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " Off with the " + combat_item)
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

    def steal(self):
        print("You steal from " + self.name)
        # How will you decide what this character has to steal?
        
# Creating a friend subclass
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.need = None
    
    def hug(self):
        print(self.name + " hugs you back!")
    # What other methods could your Friend class have?
    
    # Set the item he is looking for    
    def set_need(self, friend_need):
        self.need = friend_need
    
    # output the item he wants 
    def get_need(self):
        return self.need
    
    def reward(self, given_item):
        if given_item == self.need :
            print("You give " + self.name + " a " + given_item + ". He loves it and Hugs you")
            return True
        else:
            return False