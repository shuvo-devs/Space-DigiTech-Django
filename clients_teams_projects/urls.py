from django.urls import path
from .views import *

urlpatterns = [
    path("team/", team, name="team"),
    path("team/member/<slug:slug>", team_member, name="team_member"),
]
