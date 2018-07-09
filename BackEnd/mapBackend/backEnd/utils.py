import random, json, datetime, pytz


'''
Returns square id by a lat/lon location
'''
def get_square_id_by_location(latitude, longitude):
    return int(latitude * 3600), int(longitude * 2400)


'''
Returns a random hex-encoded color
'''
def get_random_color():
    return "#64%06x" % random.randint(0, 0xFFFFFF)  # Magic


'''
Retrieves request data
'''
def load_data(request):
    if len(request.body) > 0:
        return json.loads(request.body.decode('utf-8'))
    else:
        return request.POST


SCOREBOARD_USERS_COUNTER = 5
CHANGE_SQUARE_DELAY = 5.0  # (sec)
DEFAULT_DATETIME = datetime.datetime(2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC)
