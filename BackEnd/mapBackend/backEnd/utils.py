import random, json


'''
Returns square id by a lat/lon location
'''
def get_square_id_by_location(latitude, longitude):
    return int(latitude * 3600), int(longitude * 2400)


'''
Returns a random hex-encoded color
'''
def get_random_color():
    return "#%06xff" % random.randint(0, 0xFFFFFF)  # Magic


'''
Retrieves request data
'''
def load_data(request):
    if len(request.body) > 0:
        return json.loads(request.body.decode('utf-8'))
    else:
        return request.POST


SCOREBOARD_USERS_COUNTER = 5
