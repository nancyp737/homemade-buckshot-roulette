import random

livebullets = range(1, random.randint(2, 4))
duds = range(1, random.randint(2, 4))
gunclip = []

for live in livebullets:
    gunclip.append("live")

for dud in duds:
    gunclip.append("dud")


def checkallbullets():
    """
    doesn't take anything, just shows the bullets in a random order, will randomise again
    :return:
    the list of the gunclip
    """
    random.shuffle(gunclip)
    return print(gunclip)


def loadbullets():
    """
    "loads" bullets randomly
    :return:
    randomised and ready gunclip
    """
    random.shuffle(gunclip)
    return gunclip