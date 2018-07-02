import random


def get_square_id_by_location(latitude, longitude):
    return (int(latitude * 3600), int(longitude * 2400))


def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)  # Magic