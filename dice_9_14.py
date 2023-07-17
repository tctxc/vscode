from random import randint

class Die:
    '''创建一个骰子类'''
    def __init__(self, sides=6) -> None:
        self.sides = sides

    def roll_dice(self):
        '''投掷骰子的动作'''
        number = randint(1, self.sides)
        print(f"\tSide :{number}")

    def dice_type(self):
        '''显示使用的骰子类型'''
        print(f"\nThe type of dice is {self.sides}-sides:")


