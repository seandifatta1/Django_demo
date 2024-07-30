from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import CustomUser  # Import the custom User model
from team.models import Team

@login_required
def see_results(request):
    # Get the logged-in user
    user = request.user

    # Get the user's favorite team
    favorite_team = user.favorite_team

    # Get the conference of the favorite team
    favorite_team_conference = Team.objects.get(name=favorite_team).conference

    # Get the top 7 teams in the favorite team's conference
    conference_top_7 = list(Team.objects.filter(conference=favorite_team_conference).order_by('-wins')[:7])

    # Check if the favorite team is in the top 7 of their conference
    is_in_top_7 = any(team.name == favorite_team for team in conference_top_7)

    # Get the top 7 teams in both conferences
    afc_top_7 = list(Team.objects.filter(conference='AFC').order_by('-wins')[:7])
    nfc_top_7 = list(Team.objects.filter(conference='NFC').order_by('-wins')[:7])

    # Define the context dictionary
    context = {
        'favorite_team': favorite_team,
        'is_in_top_7': is_in_top_7,
        'conference_top_7': conference_top_7,
        'afc_top_7': afc_top_7,
        'nfc_top_7': nfc_top_7
    }

    # Render the template with the context
    return render(request, 'results/results.html', context)
