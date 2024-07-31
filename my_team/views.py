import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Team


# Create your views here.
@login_required
def team_detail(request, team_name):
    user = request.user
    favorite_team = user.favorite_team

    team_name = team_name[0].upper() + team_name[1:].lower()
    team = get_object_or_404(Team, name=favorite_team)

    teams_in_division = Team.objects.filter(division=team.division).order_by('-wins')
    all_teams = Team.objects.exclude(name=team.name)
    opponent = random.choice(all_teams)

    context = {
        'favorite_team': favorite_team,
        'teams_in_division': teams_in_division,
        'team': team,
        'opponent': opponent,
    }

    return render(request, 'my_team/my_team.html', context)


@api_view(['POST'])
def simulate_game(request):
    all_teams = list(Team.objects.all())
    random.shuffle(all_teams)

    winners = all_teams[:16]
    losers = all_teams[16:]

    for team in winners:
        team.wins += 1
        team.save()

    for team in losers:
        team.losses += 1
        team.save()

    favorite_team_name = request.data.get('favorite_team')
    favorite_team = get_object_or_404(Team, name=favorite_team_name)
    teams_in_division = Team.objects.filter(division=favorite_team.division).order_by('-wins')

    response_data = {
        'status': 'success',
        'teams_in_division': list(teams_in_division.values('name', 'wins', 'losses'))
    }

    return Response(response_data)


@api_view(['POST'])
def reset_wins_losses(request):
    teams = Team.objects.all()
    for team in teams:
        team.wins = 0
        team.losses = 0
        team.save()

    return Response({'status': 'success'})
