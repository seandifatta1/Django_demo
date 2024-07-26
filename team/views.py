from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from team.models import Team
from collections import defaultdict
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def team_view(request, team_name):
    return render(request, 'team/team_detail.html', {'team_name': team_name})


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
