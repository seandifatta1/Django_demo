from collections import defaultdict

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.models import Team

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()


@login_required
def teams(request):
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

    return render(request, 'team/teams.html', {
        'afc_teams_by_division': afc_teams_by_division,
        'nfc_teams_by_division': nfc_teams_by_division
    })

@api_view(['POST'])
def select_team(request):
    image_name = request.data.get('image_name')
    if image_name:
        if "team_logos/" in image_name:
            team_name = image_name.split("/")[1]
        else:
            team_name = image_name

        team_name = team_name.split(".")[0]

        user = request.user
        user.favorite_team = team_name
        user.save()

        return Response({'status': 'success', 'team_name': team_name})
    return Response({'status': 'failed'}, status=status.HTTP_400_BAD_REQUEST)

