from django.db.models import Count
from django.http import JsonResponse


from django.views.decorators.http import require_POST, require_GET

from BackEnd.mapBackend.backEnd.models import Square, UserProfile
from BackEnd.mapBackend.backEnd.utils import get_square_id_by_location, get_random_color


@require_POST
def add_user(request):
    data = request.POST

    user_id = data['user_id']
    new_user = UserProfile(user_id=user_id, color=get_random_color())
    new_user.save()

    return JsonResponse({
        'user_color': new_user.color
    })


@require_POST
def set_square_state(request):
    data = request.POST

    user_id = data['user_id']
    longitude = data['longitude']
    latitude = data['latitude']

    vertical_id, horizontal_id = get_square_id_by_location(longitude, latitude)
    current_square = Square.objects.get(vertical_id=vertical_id, horizontal_id=horizontal_id)
    current_square.owner = UserProfile.objects.get(user_id)
    current_square.save()

    return JsonResponse({
        'status': 'OK'
    })


@require_GET
def get_user_score(request):
    data = request.GET

    user_id = data['user_id']
    user_score = Square.objects.filter(owner=user_id).count()

    return JsonResponse({
        'user_score': user_score
    })


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
        'scoreboard': scoreboard
    })
