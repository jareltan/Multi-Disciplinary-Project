from typing import List
from entities.Entities import Cell
from constants import *

class Robot:
    def __init__(self, center_x: int, center_y: int, start_direction: Direction):
        # Robot object class
        self.states: List[Cell] = [
            Cell(center_x, center_y, start_direction)]

    def get_start_state(self):
        return self.states[0]