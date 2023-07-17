from dice_9_14 import Die #可以从“文件”或“模块”中导入“类”、“方法”、“函数”

roll_time01 = Die()
roll_time02 = Die(10)
roll_time03 = Die(20)
roll_time04 = Die(99)

roll_time01.dice_type()
for i in range(1,11):
    roll_time01.roll_dice()

roll_time02.dice_type()
for i in range(1,11):
    roll_time02.roll_dice()

roll_time03.dice_type()
for i in range(1,11):
    roll_time03.roll_dice()

roll_time04.dice_type()
for i in range(1,11):
    roll_time04.roll_dice()