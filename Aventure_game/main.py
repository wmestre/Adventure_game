# import creators for the game
from room import Room
from character import Enemy
from character import Friend
from rpginfo import RPGInfo
from item import Item, Potion

# game infos
spooky_castle = RPGInfo("The Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()
RPGInfo.author = "Drey"


# set up rooms
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty place, buzzing wtih flies.")

dining_hall = Room("Dinning_hall")
dining_hall.set_description("A large room with ornate decorations on each wall.")

ballroom = Room("ballroom")
ballroom.set_description("A vast roomm with a shiny wodden floor ; huge candlesticks guard the entrance.")

# set up characters
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

gunter = Friend("Gunter", "A mysterious dwarf")
gunter.set_conversation("I guess you are lost...")
gunter.set_need("melon")
ballroom.set_character(gunter)

# set up items
healing_potion = Potion("Healing potion")
healing_potion.set_description("A red liquid that shimmered when agitated within its vial. It has a pleasant scent of honey and orange blossoms.")
ballroom.set_item(healing_potion)

# link rooms together
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# set up character status at the begining
dead = False
good_mood = False
current_room = kitchen

backpack = ["cheese", "melon"]

print("There are " + str(Room.number_of_rooms) + " rooms to explore.")
print("There are "+ str(Item.number_of_items) + " items to find.")

# run game
while dead == False :
    
    # display informations about the current room
    print("\n")
    current_room.get_details()

    # check for inhabitant in the room
    inhabitant = current_room.get_character()
    if inhabitant is not None :
        inhabitant.describe()

    # check for items in the room
    room_item = current_room.get_item()
    if room_item is not None:
        room_item.describe()

    # Wait for input
    command = input("> ")

    # check for items in backpack
    if command == "backpack":
        if backpack:
            print("Items collected : " + ', '.join(backpack))
        else :
            print("Nothing in your backpack.")
    
    # move to an other room
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    
    # talk to the inhabitant
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There is nobody in this room...")

    # fight with the inhabitant
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input("> ")
            if fight_with in backpack:
                backpack.remove(fight_with)
                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.set_character(None)
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight")
                    print("That's the end of the game")
                    dead = True
            else:
                print("There is no " + fight_with + " in your backpack.")
        else:
            print("There is no one here to fight with") 
    
    # give an item to the friendly character
    elif command == "give":
        if inhabitant is not None :
            if isinstance(inhabitant, Enemy):
                print("That may not be a good idea...")
            else :
                if good_mood == False :
                    # you haven't already given the right present
                    given = input("What do you want to give to " + inhabitant.name + " ?")
                    if inhabitant.reward(given) == True :
                        # What happens if it is the right present ?
                        print(inhabitant.name + " gives you a key !")
                        good_mood = True
                    else :
                        # What happens if it is not the right present ?
                        print(inhabitant.name + "Doesn't liked your present, He is offended.")
                elif good_mood == True:
                    # You already gave the right present
                    print(inhabitant.name + " has no needs.") 
        else : 
            print("Nobody is here..")
    
    # give a hug to the friendly character
    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.hug()
        else:
            print("There is no one here to hug :(")

    # take an object
    elif command == "take":
        if room_item is not None:
            backpack.append(room_item.name)
            current_room.set_item(None)
        else:
            print("No item here..")

RPGInfo.credits()