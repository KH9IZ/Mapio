from django.db.models import Count, Q
from django.http import JsonResponse


from django.views.decorators.http import require_POST, require_GET

from backEnd.models import Square, UserProfile
from backEnd.utils import get_square_id_by_location, get_random_color

'''
API documentation at https://docs.google.com/document/d/1pbdqBmTb9zvqssmj4nSL7hbwmlvXY7tLn7uxyroTjP0/edit
TODO Check lat/lon consistency !important
'''

'''
TODO Think about security
Adds user to db on first login
'''
@require_POST
def add_user(request):
    data = request.POST

    user_id = data['user_id']
    new_user = UserProfile(user_id=user_id, color=get_random_color())
    new_user.save()

    return JsonResponse({
        'user_color': new_user.color,
    })

'''
TODO Paint area on crossing user's existing path
Resets square owner
'''
@require_POST
def set_square_state(request):
    data = request.POST

    user_id = data['user_id']
    latitude = data['latitude']
    longitude = data['longitude']

    vertical_id, horizontal_id = get_square_id_by_location(latitude, longitude)
    if Square.objects.exists(vertical_id=vertical_id, horizontal_id=horizontal_id):  # Check if this square exists already
        current_square = Square.objects.get(vertical_id=vertical_id, horizontal_id=horizontal_id)
        current_square.owner = UserProfile.objects.get(user_id=user_id)
        current_square.save()
    else:
        current_square = Square(vertical_id=vertical_id,
                                horizontal_id=horizontal_id,
                                owner=UserProfile.objects.get(user_id=user_id))
        current_square.save()

    return JsonResponse({
        'status': 'OK',
    })

'''
TODO For later versions
TODO 0 meridian error
'''
@require_GET
def get_frame_data(request):
    data = request.GET
    response = []

    bottom_left_longitude = data['bottom_left_corner']['longitude']
    bottom_left_latitude = data['bottom_left_corner']['latitude']
    top_right_longitude = data['top_right_corner']['longitude']
    top_right_latitude = data['top_right_corner']['latitude']

    bottom_left_vertical_id, bottom_left_horizontal_id = get_square_id_by_location(bottom_left_latitude,
                                                                                   bottom_left_longitude)
    top_right_vertical_id, top_right_horizontal_id = get_square_id_by_location(top_right_latitude,
                                                                               top_right_longitude)

    for square in Square.objects.filter(horizontal_id__gte=bottom_left_horizontal_id,
                                        horizontal_id__lte=top_right_horizontal_id,
                                        vertical_id__gte=bottom_left_vertical_id,
                                        vertical_id__lte=top_right_vertical_id):
        response.append({'horizontal_id': square.horizontal_id,
                         'vertical_id': square.vertical_id,
                         'color': square.owner.color})
    return JsonResponse({
        'squares': response
    })


'''
TODO
/get_frame_data temporary replacement
'''
@require_GET
def get_squares_data(request):
    raw_squares = Square.objects.all()
    squares = []

    for square in raw_squares:
        squares.append({
            'vertical_id': square.vertical_id,
            'horizontal_id': square.horizontal_id,
            'color': square.owner.color,
        })


'''
Returns user's score
'''
@require_GET
def get_user_score(request):
    data = request.GET

    user_id = data['user_id']
    user_score = Square.objects.filter(owner=user_id).count()

    return JsonResponse({
        'user_score': user_score,
    })


'''
Returns top 5 users
'''
@require_GET
def get_scoreboard(request):
    raw_scoreboard = UserProfile.objects.annotate(score=Count('UserProfile__Square')).\
        order_by('-score')[:5]

    scoreboard = []
    for current_user in raw_scoreboard:
        scoreboard.append({
            'user_id': current_user.user_id,
            'user_score': current_user.get_user_score(),
        })

    return JsonResponse({
        'scoreboard': scoreboard,
    })


'''
Returns nearest grid square
'''
@require_GET
def get_nearest_square(request):
    data = request['GET']

    latitude = data['latitude']
    longitude = data['longitude']

    vertical_id, horizontal_id = get_square_id_by_location(latitude, longitude)

    return JsonResponse({
        'nearest_latitude': vertical_id,
        'nearest_longitude': horizontal_id,
    })

@require_GET
def get_user_color(request):
    data = request.GET

    user_id = data['user_id']
    user_color = UserProfile.objects.get(user_id=user_id).color

    return JsonResponse({
        'user_color': user_color,
    })