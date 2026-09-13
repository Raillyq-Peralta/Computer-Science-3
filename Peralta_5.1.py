# HERO CLASS
class Hero:
    # ATTRIBUTES
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    # METHODS
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0  

# HERO INITIALIZATION
arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

# DAMAGE DEFINITION
arthur.take_damage(10)

# HEALTH DISPLAY
print(f"Arthur's HP: {arthur.hp}")
print(f"Morgana's HP: {morgana.hp}")

# CHALLENGE THINKING QUESTION
'''

'''