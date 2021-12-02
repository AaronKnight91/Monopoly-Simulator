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
        self._in_jail = False

    def update_position(self, dice_roll):

        self.position += dice_roll
        if self.position % 39 > 0:
            self._pass_go = True
            self.position = self.position % 40

    def go_to_jail(self):

        if self.position == 30:
            self._in_jail = True
            self.position = 10

    
def main():

    player = Player()

    for i in range(10):
        dice = DiceRoll()
        player.update_position(dice.roll)

if __name__ == "__main__":
    main()
