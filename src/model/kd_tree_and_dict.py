import numpy as np
from scipy.spatial import cKDTree

from .ant import Ant
from .food import Food
from .nest import Nest
from .world import World


class KdTreeAndDict(World):

    """
            A class used to implement the tree and dictionary in the game (alternative to gird)
            It inherits from World class

            ...

            Attributes
            ----------
            all_objects: dict
                a dictionary for all the objects in the game
            kd_tree: cKDTree
                a tcKDTree implementation for nearest neighbours
            point_matrix: array
                an ### Add this

    """

    def __init__(self):
        self.all_objects = {}
        # TODO: check if None declaration
        # will not make trouble later
        self.kd_tree = None
        self.point_matrix = None

    def get_k_nearest(self, position, k=1):
        """ Get k nearest neighbour ants for specific position using kd_tree that uses Euclidean distance.

        :param position: (list) Coordinates of the position to which the nearest neighbours are calculated.
        :param k: (int) Number of nearest neighbours
        :return point_matrix: (array) ### Add this
        :return dists: (array of floats) Distances to the nearest neighbours

        """
        # TODO: can multithread if called with many params and -1
        dists, idx = self.kd_tree.query(np.array(position), k, p=2)
        return self.point_matrix[idx], dists

    def get_at_position(self, position):
        """ Return all the objects (ants/food/nest) in specific position

        :param position: (list) Coordinates of specific position
        :return: (list) ALL objects in the given position

        """
        return self.all_objects.get(position)

    def get_rectangle_region(self, top_left, bottom_right):
        """

        :param top_left: (list) Coordinates of top left point of the rectangle
        :param bottom_right: (list) Coordinates of bottom right point of the rectangle
        :return:

        """
        top_left = np.array(top_left)
        bottom_right = np.array(bottom_right)
        longest_side = np.max(bottom_right[0] - top_left[0], top_left[1] - bottom_right[1])
        center = (np.array(top_left) - np.array(bottom_right)) / 2
        large_square = self.get_square_region(center, longest_side)

        x_min = top_left[0]
        y_min = bottom_right[1]
        x_max = bottom_right[0]
        y_max = top_left[0]

        bool_idx = [self._is_in_rectangle(position, x_min, x_max, y_min, y_max) for position in large_square]
        return large_square[bool_idx]

    def get_circular_region(self, center, radius):
        position_idx = self.kd_tree.query_ball_point(center, radius, p=2)
        positions = self.point_matrix[position_idx]
        result = []
        for position in positions:
            result.extend(self.all_objects.get(position, []))
        return result

    def get_k_nearest_list(self, position_list, k_list):
        # TODO: can multithread if called with many params and -1
        idx_list = self.kd_tree.query(np.array(position_list), k_list, p=2)
        result = []
        for idx in idx_list:
            result.append(self.point_matrix[idx])
        return result

    def get_rectangle_region_list(self, top_left_list, bottom_right_list):
        #
        pass

    def get_circular_region_list(self, center_list, radius_list):
        position_idx_list = self.kd_tree.query_ball_point(center_list, radius_list, p=2)
        result = []
        for position_idx in position_idx_list:
            positions = self.point_matrix[position_idx]
            sub_result = []
            for position in positions:
                sub_result.extend(self.all_objects.get(position, []))
            result.append(sub_result)
        return result

    def update(self):
        pass

    def create_nests(self, color_list, position_list, size, health):
        for position, color in zip(position_list, color_list):
            self.all_objects.setdefault(position, []).append(Nest(position, color, size, health))
        self._update_tree()

    def create_ants(self, nest, amount):
        position = nest.position
        color = nest.color
        for _ in range(amount):
            self.all_objects.setdefault(position, []).append(Ant(color, position))
        self._update_tree()

    def create_food(self, position_list, size_list):
        # TODO: compare to extend with food list
        for position, size in zip(position_list, size_list):
            self.all_objects.setdefault(position, []).append(Food(position, size))
        self._update_tree()

    def _update_tree(self):
        keys = list(self.all_objects.keys())
        self.point_matrix = np.array(keys)
        self.kd_tree = cKDTree(self.point_matrix)

    def get_square_region(self, center, radius):
        position_idx = self.kd_tree.query_ball_point(center, radius, p=np.inf)
        positions = self.point_matrix[position_idx]
        result = []
        for position in positions:
            result.extend(self.all_objects.get(position, []))
        return result

    def _is_in_rectangle(self, position, x_min, x_max, y_min, y_max):
        return x_min <= position[0] <= x_max and y_min <= position[1] <= y_max
