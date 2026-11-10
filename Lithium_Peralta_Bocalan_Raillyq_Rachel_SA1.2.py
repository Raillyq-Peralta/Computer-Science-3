# COMPUTER SCIENCE 3
# HANDS-ON ASSESSMENT: RPG BATTLE ARENA

#Place your name/s here: Raillyq Peralta | Rachel Bocalan
#Place your section here:9 - Lithium
#Place your date here: 11-10-26

# ===== KNIGHT CLASS =====
class Knight:
    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage

    def get_name(self):
        # TODO 1: Return the private name
        return self.__name

    def get_damage(self):
        # TODO 2: Return the private damage
        return self.__damage

    def set_damage(self, new_damage):
        # TODO 3: Update damage only if
        # the new value is greater than 0
        if new_damage > 0:
          self.__damage = new_damage

    def attack(self):
        print(f"{self.get_name()} swings his sword!")
        # TODO 4: Return the character's damage
        print(f"Damage dealt: {self.get_damage()}")
        return self.get_damage()


# ===== WIZARD CLASS =====
class Wizard:
    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage

    def get_name(self):
        # TODO 5: Return the private name
        return self.__name

    def get_damage(self):
        # TODO 6: Return the private damage
        return self.__damage

    def set_damage(self, new_damage):
        # TODO 7: Update damage only if
        # the new value is greater than 0
        if new_damage > 0:
          self.__damage = new_damage

    def attack(self):
        print(f"{self.get_name()} casts a fireball!")
        # TODO 8: Return the character's damage
        print(f"Damage dealt: {self.get_damage()}")
        return self.get_damage()


# ===== ASSASSIN CLASS =====
class Assassin:
    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage

    def get_name(self):
        # TODO 9: Return the private name
        return self.__name

    def get_damage(self):
        # TODO 10: Return the private damage
        return self.__damage

    def set_damage(self, new_damage):
        # TODO 11: Update damage only if
        # the new value is greater than 0
        if new_damage > 0:
          self.__damage = new_damage

    def attack(self):
        print(f"{self.get_name()} performs a strike!")
        # TODO 12: Return the character's damage
        print(f"Damage dealt: {self.get_damage()}")
        return self.get_damage()


# ===== POLYMORPHIC FUNCTION =====
def perform_attack(character):
    # TODO 13: Call attack() and store
    # its returned value in damage
    character.attack()
    # TODO 14: Display "Damage dealt: "
    # followed by the damage value
    # TODO 15: Return the damage
    damage = character.attack()
    return damage

# ===== CREATE OBJECTS =====
# TODO 16: Create the following objects:
# knight = Knight("Arthur", 25)
# wizard = Wizard("Merlin", 40)
# assassin = Assassin("Shadow", 35)
knight = Knight("Arthur", 25)
wizard = Wizard("Merlin", 40)
assassin = Assassin("Shadow", 35)
# ===== GETTER AND SETTER TEST =====
print("===== CHARACTER UPDATE =====")

# TODO 17: Increase wizard damage to 50
# using the setter method
wizard.set_damage(50)

# TODO 18: Try setting knight damage to -10
# using the setter method
knight.set_damage(-10)

# TODO 19: Display wizard and knight damage
# using their getter methods
print(f"Wizard Damage: {wizard.get_damage()}")
print(f"Knight Damage: {knight.get_damage()}")
# ===== CHARACTER LIST =====
# TODO 20: Store the three objects
# in a list named characters
characters = [knight, wizard, assassin]


# ===== BATTLE SYSTEM =====
print("\n===== RPG BATTLE ARENA =====")

total_damage = 0

# TODO 21: Use a for loop to call
# perform_attack() for every character
# and add the returned damage to total_damage
for character in characters:
  perform_attack(character)
  total_damage += perform_attack(character)


# ===== BATTLE RESULTS =====
print("--------------------------")
print("Total Damage:", total_damage)
print("Enemy Health: 100")

# TODO 22: Use if-else to display:
# Victory! The enemy has been defeated!
# OR
# Defeat! The enemy is still standing!
if total_damage >= 100:
  print("Victory! The enemy has been defeated!")
else:
  print("Defeat! The enemy is still standing!")
