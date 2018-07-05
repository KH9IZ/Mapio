from django.conf.urls import url
from django.contrib import admin

from backEnd.views import set_square_state, add_user, get_user_score, get_scoreboard, \
    get_nearest_square, get_user_color, drop_bomb, get_frame_data, get_squares_data

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get_frame_data', get_frame_data),
    url(r'^get_squares_data', get_squares_data),
    url(r'^send_user_coordinates/', set_square_state),
    url(r'^add_user/', add_user),
    url(r'^get_user_score/', get_user_score),
    url(r'^get_scoreboard', get_scoreboard),
    url(r'^get_nearest_square', get_nearest_square),
    url(r'^get_user_color', get_user_color),
    url(r'^drop_bomb', drop_bomb)
]
