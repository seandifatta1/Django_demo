from django.urls import path

from . import views

team_names = [
    "cardinals",
    "falcons",
    "ravens",
    "bills",
    "panthers",
    "bears",
    "bengals",
    "browns",
    "cowboys",
    "broncos",
    "lions",
    "packers",
    "texans",
    "colts",
    "jaguars",
    "chiefs",
    "raiders",
    "chargers",
    "rams",
    "dolphins",
    "vikings",
    "patriots",
    "saints",
    "giants",
    "jets",
    "eagles",
    "steelers",
    "49ers",
    "seahawks",
    "buccaneers",
    "titans",
    "commanders"
]

urlpatterns = [
    path(f'teams/{team_name}/', views.team_detail, {'team_name': team_name}, name=f'{team_name}_page') for team_name in team_names
] + [
    path('teams/', views.team_list, name='team_list'),
    path('select_team/', views.select_team, name='select_team'),
    path('simulate_game/', views.simulate_game, name='simulate_game'),
    path('reset_wins_losses/', views.reset_wins_losses, name='reset_wins_losses'),
]