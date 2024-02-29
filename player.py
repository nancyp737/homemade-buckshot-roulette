class Player:
    """
    just to create the player
     """

    def __init__(self):
        self.health = 100

    def gethealth(self):
        """
        get the health of the character
        :return:
        health value
        """
        return self.health

    def sethealth(self, new):
        """
        set the health
        :param new:
        new health value
        """
        self.health = new
