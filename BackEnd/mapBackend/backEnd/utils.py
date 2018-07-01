import random


def get_square_id_by_location(longitude, latitude):
    return (longitude // (360 * 60 * 60), latitude // (260 * 60 * 60))


def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)  # Magic