import random


'''
Returns square id by a lat/lon location
'''
def get_square_id_by_location(latitude, longitude):
    return int(latitude * 3600), int(longitude * 2400)


'''
Returns a random hex-encoded color
'''
def get_random_color():
    return "#%06x64" % random.randint(0, 0xFFFFFF)  # Magic


SCOREBOARD_USERS_COUNTER = 5