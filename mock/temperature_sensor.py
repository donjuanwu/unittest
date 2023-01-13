"""
Reading temperature from random()
Reference: Homework 1
"""

import random


def read_temperature():
    """
    simulates a temperature sensor by returning random temperature values
    :return: -10 - 110 F
    """
    return random.randint(-10, 110)
