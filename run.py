import pandas as pd
from random import randint

class DiceRoll():

    def __init__(self):

        self._dice_1 = self.roll_die()
        self._dice_2 = self.roll_die()

        self.roll = self.sum_die()

        self.double_roll = self.check_double_roll()

    def roll_die(self):

        return randint(1, 7)

    def sum_die(self):

        return self._dice_1 + self._dice_2

    def check_double_roll(self):

        if self._dice_1 == self._dice_2:
            return True
        else:
            return False

class Player():

    def __init__(self):

        self.position = 0
        self._passed_go = False

        self.money = 1500
        
        self._in_jail = False
        self._breakout_attempts = 0

    def update_position(self, dice):

        self.position += dice.roll
        if self.position % 39 > 0:
            self._pass_go = True
            self.earn_money(200)
            self.position = self.position % 40

        # Pay Tax
        if self.position == 4:
            self.pay_money(200)
        # Pay Super Tax
        if self.position == 38:
            self.pay_money(100)

    def go_to_jail(self):

        if self.position == 30:
            self._in_jail = True
            self.position = 10

    def get_out_of_jail(self, dice):

        if self._in_jail:
            if dice.double_roll:
                self._in_jail = False
            else:
                self._breakout_attempts += 1
                if self._breakout_attempts == 3:
                    if self.pay_money(50):
                        self._in_jail = False

    def earn_money(self, value):

        self.money += value
                        
    def pay_money(self, value):

        if (self.money - value) > 0:
            self.money -= value
            return True
        else:
            return False

    def buy_property(self, board):

        if self._passed_go:
            self.pay_money(board.loc[self.position]["Price"])

            return True

        else:
            return False

class Board():

    def __init__(self):

        self.board = pd.read_csv("board_data_sheet.csv")
        self.board.set_index("Number", inplace=True)
        self.board["Owned"] = ""

    def can_be_bought(self, position):

        if self.board.loc[position]["Price"] > 0:
            return True
        else:
            return False
        
    def update_owned_status(self, position):

        self.board.loc[position]["Owned"] = True
        
            
def main():

    player = Player()
    board = Board()
        
    for i in range(10):
        dice = DiceRoll()
        player.update_position(dice)
        if board.can_be_bought(player.position):
            bought = player.buy_property(board)

            if bought:
                board.update_owned_status(player.position)

if __name__ == "__main__":
    main()
