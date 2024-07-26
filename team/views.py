# Create your views here.
import random
from collections import defaultdict

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Team

# from ../..

User = get_user_model()


def team_detail(request, team_name):
    # Get the favorite team for the user
    user = request.user
    favorite_team = user.favorite_team

    # Ensure the team_name is properly formatted
    team_name = team_name[0].upper() + team_name[1:].lower()
    team = get_object_or_404(Team, name=team_name)

    # Get the teams in the same division sorted by wins in descending order
    teams_in_division = Team.objects.filter(division=team.division).order_by('-wins')

    # Select a random opponent from the teams in the same division, excluding the favorite team
    opponent = random.choice([t for t in teams_in_division if t.name != team_name])

    context = {
        'favorite_team': favorite_team,
        'teams_in_division': teams_in_division,
        'team': team,
        'opponent': opponent,
    }

    return render(request, 'team/team_detail.html', context)


def team_list(request):
    teams = Team.objects.all().values('division', 'logo_path')

    # Grouping teams by division
    teams_by_division = defaultdict(list)
    for team in teams:
        teams_by_division[team['division']].append(team['logo_path'])

    # Converting defaultdict to a regular dict for easier template usage
    teams_by_division = dict(teams_by_division)

    return render(request, 'team/team_list.html', {'teams_by_division': teams_by_division})


# @login_required
def handle_click(request):
    if request.method == 'POST':
        image_name = request.POST.get('image_name')
        if image_name:

            if "team_logos/" in image_name:
                team_name = image_name.split("/")[1]
            else:
                team_name = image_name

            # Extract team name from image_name
            team_name = team_name.split(".")[0]

            # Update the favorite_team field for the current user
            user = request.user
            user.favorite_team = team_name
            user.save()

            # Redirect to the team-specific page
            # return redirect(f'/teams/{team_name}/')
            return JsonResponse({'status': 'success', 'team_name': team_name})
    return JsonResponse({'status': 'failed'})
