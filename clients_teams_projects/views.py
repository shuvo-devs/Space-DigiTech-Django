from django.shortcuts import render, get_object_or_404
from .models import Team
from pages.models import TeamPage


def team(request):
    try:
        team_page = TeamPage.get_solo()
    except TeamPage.DoesNotExist:
        team_page = None
    team = Team.objects.all()

    data = {
        "team_page": team_page,
        "team": team,
    }
    return render(request, "pages/team.html", data)


def team_member(request, slug):
    team_member = get_object_or_404(Team, slug=slug)

    data = {
        "team_member": team_member,
    }
    return render(request, "pages/team_member.html", data)
