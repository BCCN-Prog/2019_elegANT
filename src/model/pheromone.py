from .game_object import GameObject


class Pheromone(GameObject):
    """
            A class used to represent a nest object
            It inherits from GameObject class

            ...

            Attributes
            ----------
            position: ndarray
            color: tuple of ints
                tuple containing the (R,G,B) values
            strength: float
                a number that specifies the pheromone level at this position
    """

    def __init__(self, position, color, initial_strength=1.):
        """

        :param position: (list) coordinates of the nest
        :param color: (tuple) (R,G,B) color code for the pheromone
        :param inital_strength: inital strength value, decays afterwards
        """
        super(Pheromone, self).__init__(position)
        self.color = color
        self.strength = initial_strength

    def update(self, *args):
        self._decay()
        # TODO: use another cutoff value for pheromone disappearance
        if self.strength <= 1e-8:
            self.strength = 0.
            return None
        else:
            return self.position

    def increase(self, added_strength=1.):
        if added_strength <= 0.:
            raise ValueError('This function should not be used to decrease pheromone strength (or leave it unchanged)')
        self.strength += added_strength

    def _decay(self):
        # TODO decide on another decaying scheme
        self.strength = 0.75 * self.strength
