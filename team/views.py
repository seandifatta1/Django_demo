import random
from collections import defaultdict

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import json

from .models import Team

User = get_user_model()

import random

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

    return render(request, 'team/team_detail.html', context)


def team_list(request):
    teams = Team.objects.all().values('division', 'logo_path', 'conference')

    afc_teams_by_division = defaultdict(list)
    nfc_teams_by_division = defaultdict(list)

    for team in teams:
        if team['conference'] == 'AFC':
            afc_teams_by_division[team['division']].append(team['logo_path'])
        elif team['conference'] == 'NFC':
            nfc_teams_by_division[team['division']].append(team['logo_path'])

    afc_teams_by_division = dict(sorted(afc_teams_by_division.items()))
    nfc_teams_by_division = dict(sorted(nfc_teams_by_division.items()))

    return render(request, 'team/team_list.html', {
        'afc_teams_by_division': afc_teams_by_division,
        'nfc_teams_by_division': nfc_teams_by_division
    })
def handle_click(request):
    if request.method == 'POST':
        image_name = request.POST.get('image_name')
        if image_name:
            if "team_logos/" in image_name:
                team_name = image_name.split("/")[1]
            else:
                team_name = image_name

            team_name = team_name.split(".")[0]

            user = request.user
            user.favorite_team = team_name
            user.save()

            return JsonResponse({'status': 'success', 'team_name': team_name})
    return JsonResponse({'status': 'failed'})

def simulate_game(request):
    if request.method == 'POST':
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

        favorite_team_name = json.loads(request.body).get('favorite_team')
        favorite_team = get_object_or_404(Team, name=favorite_team_name)
        teams_in_division = Team.objects.filter(division=favorite_team.division).order_by('-wins')

        response_data = {
            'status': 'success',
            'teams_in_division': list(teams_in_division.values('name', 'wins', 'losses'))
        }

        return JsonResponse(response_data)
    return JsonResponse({'status': 'failed'}, status=400)

def reset_wins_losses(request):
    if request.method == 'POST':
        teams = Team.objects.all()
        for team in teams:
            team.wins = 0
            team.losses = 0
            team.save()

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)