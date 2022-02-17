from character import Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.describe()

# Add some conversation for Dave when he is talked to
dave.set_conversation("Grawrrrr... I'm Daah..ve.... How are You ?")

# Trigger a conversation with Dave
dave.talk()
dave.set_weakness("cheese")

print(dave.get_weakness())

# Fight with Dave
print("What will you fight with ?")
fight_with = input("> ")
dave.fight(fight_with)
