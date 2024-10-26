#################################################################################################################################################################################################################
# FIELDS
#################################################################################################################################################################################################################
# Base Imports

import random
import time
import json

#################################################################################################################################################################################################################
# Load card templates from JSON

def load_card_templates(file_path):
    """Load card templates from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

card_templates = load_card_templates('card_templates.json')

#################################################################################################################################################################################################################
# Base Classes

class Card:
    def __init__(self, card_template):
        self.template_id = card_template["card_template_id"]
        self.name = card_template["name"]
        self.health = card_template["health"]
        self.attack = card_template["attack"]
        self.cost = card_template["cost"]
        self.ability = card_template["abilities"]
        self.move = card_template["move"]
        self.type = card_template["type"]

    def print(self):
        name_line_1 = self.name[:9]
        name_line_2 = self.name[9:18] 
        # Card visual structure
        print(f"+-{self.type:<7}-+")  
        print(f"|{name_line_1:<9}|") 
        print(f"|{name_line_2:<9}|") 
        print(f"|H:{self.health:<2} A:{self.attack:<2}|") 
        print(f"|M:{self.move:<2} C:{self.cost:<2}|")
        print(f"|{self.ability[:9]:<9}|") 
        print("+---------+") 

class Player:
    def __init__(self, name, card_templates):
        self.name = name
        self.card_templates = card_templates
        self.deck = []
        self.hand = []
        self.health = 10  
        self.create_deck()
        self.shuffle_deck()

    def create_deck(self):
        """Create a deck with 2 copies of each card template."""
        for template in self.card_templates:
            self.deck.append(Card(template))  # First copy of the card
            self.deck.append(Card(template))  # Second copy of the card

    def shuffle_deck(self):
        """Shuffle the deck of cards."""
        random.shuffle(self.deck)

    def draw_cards(self, num_cards):
        """Draw num_cards from the deck to the player's hand."""
        for _ in range(num_cards):
            if self.deck:  # Ensure there are cards left in the deck
                self.hand.append(self.deck.pop())

    def show_hand(self):
        """Display the cards in the player's hand in an ASCII card format."""
        print(f"----------------------------{self.name}--{self.health}------------------------")
        card_lines = [[] for _ in range(7)]  # Create a list to store each line of the card representation

        for card in self.hand:
            name_line_1 = card.name[:9]  # First 9 characters of the name
            name_line_2 = card.name[9:18]  # Next 9 characters of the name (if available)

            # Card visual structure
            card_lines[0].append(f"+-{card.type:<7}-+")  # Top border of card
            card_lines[1].append(f"|{name_line_1:<9}|")  # First line of the name (up to 9 characters)
            card_lines[2].append(f"|{name_line_2:<9}|") 
            card_lines[3].append(f"|H:{card.health:<2} A:{card.attack:<2}|")  # Health and Attack
            card_lines[4].append(f"|M:{card.move:<2} C:{card.cost:<2}|")  # Move and Cost
            card_lines[5].append(f"|{card.ability[:9]:<9}|")  # Ability (limited to 9 characters)
            card_lines[6].append("+---------+")  # Bottom border of card

        for line in card_lines:
            print("  ".join(line))  # Print each card line next to each other

class Com(Player):
    def __init__(self, card_templates):
        super().__init__("Computer", card_templates)

class Field:
    def __init__(self):
        # Initialize a 4x4 grid for the field (None indicates an empty spot)
        self.field = [[None for _ in range(4)] for _ in range(4)]

    def place_card(self, card, x, y):
        """Place a card at specific coordinates (x, y) on the 4x4 field."""
        if 0 <= x < 4 and 0 <= y < 4:  # Ensure the coordinates are within the 4x4 grid
            self.field[x][y] = card
        else:
            print(f"Invalid coordinates: ({x}, {y})")

    def display_field(self):
        print(f"----------------------------FIELD----------------------------")
        """Display the 4x4 field with cards based on their positions."""
        
        for row in self.field:
            row_card_lines = [[] for _ in range(7)]  # Temporary list to store the lines for a single row of cards

            for card in row:
                if card:
                    name_line_1 = card.name[:9]  
                    name_line_2 = card.name[9:18]  
                    card_lines = [
                        f"+-{card.type:<7}-+", 
                        f"|{name_line_1:<9}|", 
                        f"|{name_line_2:<9}|", 
                        f"|H:{card.health:<2} A:{card.attack:<2}|", 
                        f"|M:{card.move:<2} C:{card.cost:<2}|", 
                        f"|{card.ability[:9]:<9}|",  
                        "+---------+"  
                    ]
                else:
                    card_lines = [
                        "+---------+",
                        "|         |",
                        "|   Empty |",
                        "|         |",
                        "|         |",
                        "|         |",
                        "+---------+"
                    ]
                for i in range(7):
                    row_card_lines[i].append(card_lines[i])
            for i in range(7):
                print("  ".join(row_card_lines[i]))  
#################################################################################################################################################################################################################
# Base Functions
def start_duel():
    """Initiates a duel by setting up decks, shuffling, and drawing hands."""
    print("Starting the duel...")

    # Create players
    player1 = Player("Player", card_templates)  #later player_deck
    com = Com(card_templates)                   #later com_deck(level)

    player1.draw_cards(4)
    com.draw_cards(4)

    player1.show_hand()
    com.show_hand()

    field = Field()

    # Place two cards on the field for demons
    # tration (positions: 0,0 and 1,1)
    # field.place_card(player1.hand[0], 0, 0)
    # field.place_card(com.hand[0], 1, 1)

    field.display_field()

# TYPES PROTOYPE
#  PSI:

#     Beats: Shadow, Stone
#     Weak against: Wind, Fire

# Shadow:

#     Beats: Stone, Water
#     Weak against: PSI, Fire

# Stone:

#     Beats: Water, Wind
#     Weak against: Shadow, PSI

# Water:

#     Beats: Wind, Fire
#     Weak against: Stone, Shadow
	
# Wind:

#     Beats: Fire, PSI
#     Weak against: Water, Stone

# Fire:

#     Beats: PSI, Wind
#     Weak against: PSI, Shadow
	
	
#################################################################################################################################################################################################################
# Base Script
start_duel()
