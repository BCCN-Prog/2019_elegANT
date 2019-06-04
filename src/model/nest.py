from .game_object import GameObject


class Nest(GameObject):
    """
            A class used to represent a nest object
            It inherits from GameObject class

            ...

            Attributes
            ----------
            position: list
                a list of all coordinates of nest position
            player: Player object owning the nest
                a string for the nest color
            size: int
                a number for the radius of the nest
            health: int
                a number that specifies the health of the nest
            food: int
                a number that specifies amount of food in the nest
            ant_ids: list
                a list of all the ants IDs that beling to this nest

    """

    def __init__(self, position, player, size, health):
        """

        :param position: (list) coordinates of the nest
        :param color: ((R,G,B) tuple) color of the nest
        :param size: (int) radius of the nest
        :param health: (int) health if the nest
        """
        super(Nest, self).__init__(position)
        # TODO: also needs id
        self.owner = player
        self.size = size
        self.health = health
        self.food = 0
        self.ant_ids = set()

    def increase_food(self, food_amount):
        """ Increase the food level by the added food_amount to the nest

        :param food_amount: (int) quantity of the food that should be added to the nest
        :return:

        """
        self.food += food_amount
        return self.food

    def create_ant(self):
        """ Create new ant to this nest after checking if the nest has enough food.

        :return:

        """
        ant_cost = 1
        if self.food >= ant_cost:
            self.food -= ant_cost
            # Generate ant at position in nest.

    def decrease_health(self, damage):
        """ Reduce the health of the nest in case of attack

        :param damage: () extent of nest damage caused by attack
        :return:

        """
        self.health -= damage
        if self.health <= 0:
            print("Oh no, your colony has a problem!")
            # TODO: remove colony

    def get_number_of_ants(self):
        """ Get the number of ants in this nest

        :return: (int) number of ants in the nest

        """
        return len(self.ant_ids)

    def update(self, *args):
        if self.health <= 0:
            return None
        else:
            return self.position
