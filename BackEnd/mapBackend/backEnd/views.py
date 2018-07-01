from django.http import JsonResponse

# Create your views here.
from django.views.decorators.http import require_POST

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