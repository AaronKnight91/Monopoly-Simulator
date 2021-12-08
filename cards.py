import pandas as pd

class Cards():

    def __init__(self, file):

        self.cards = self.get_card_deck(file)
        
    def get_cards_deck(file):
        
        return pd.read_csv(file)

    def shuffle_cards(self):

        self.cards["Cards"](frac=1).reset_index(drop=True)

    def draw_card(self):

        tmp = self.card["Cards"].iloc[0]
        self.cards["Cards"].drop(self.card["Cards"].iloc[0], inplace=True)
        return tmp

    def replace_card(self, card):

        self.cards.append(card)

class ChanceCards(Cards):

    def __init__(self, file):

        Cards.__init__(self)

class CommunityChestCards(Cards):

    def __init__(self, file):

        Cards.__init__(self)
