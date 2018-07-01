from django.conf.urls import url
from django.contrib import admin

from BackEnd.mapBackend.backEnd.views import set_square_state, add_user, get_user_score, get_scoreboard

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^send_user_coordinates/', set_square_state),
    url(r'^add_user/', add_user),
    url(r'^get_user_score/', get_user_score),
    url(r'^get_scoreboard', get_scoreboard),
]
