#################################################################################################################################################################################################################
# FIELDS
#################################################################################################################################################################################################################
# Base Imports

import random 
import time

#################################################################################################################################################################################################################
# Base Parameters

import random 
import time

card_templates = [
    {
        'name': 'warrior',
        'health': random.randint(1, 3),
        'attack': random.randint(1, 5),
        'move': random.randint(1, 3),
        'ability': 'none',
        'template_id': 1
    },
    {
        'name': 'thief',
        'health': random.randint(1, 2),
        'attack': random.randint(1, 3),
        'move': random.randint(2, 4),
        'ability': 'stealth',
        'template_id': 2
    },
]

#################################################################################################################################################################################################################
# Base Classes

class Card:
    def __init__(self, card_templates):
        self.card_templates = card_templates
        self.create_card()

    def create_card(self):
        # Randomly select a card template from the array
        selected_template = random.choice(self.card_templates)

        # Create a new card with the selected template's properties
        self.template_id = selected_template.get("template_id", random.randint(1, 100))  # Giving random template_id if not in template
        self.name = selected_template["name"]
        self.health = selected_template["health"]
        self.ability = selected_template["ability"]
        self.move = selected_template["move"]

    def print(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Move: {self.move}")
        print(f"Ability: {self.ability}")

# class Player:

#     def __init__(self):
#         self.create_player()

#     def create_player(self):
#         self.id #number
#         self.name #string
#         self.hand #array of cards
#         self.health #number

# class Com:
    
#     def __init__(self):
#         self.create_com()

#     def create_com(self):
#         self.id #number
#         self.name #string
#         self.hand #array of cards
#         self.health #number

class Field:
    def __init__(self, card_templates):
        self.card_templates = card_templates
        self.create_card()

    def create_card(self):
        # Randomly select a card template from the array
        selected_template = random.choice(self.card_templates)

        # Create a new card with the selected template's properties
        self.template_id = selected_template.get("template_id", random.randint(1, 100))  # Giving random template_id if not in template
        self.name = selected_template["name"]
        self.health = selected_template["health"]
        self.ability = selected_template["ability"]
        self.move = selected_template["move"]

#################################################################################################################################################################################################################
# Base Functions

#################################################################################################################################################################################################################
# Base Script

# player1 = Player()
# com = Com()

card = Card(card_templates)

card.print()

