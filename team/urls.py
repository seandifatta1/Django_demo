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
    path(f'teams/{team_name}/', views.team_detail, {'team_name': team_name}, name=f'{team_name}_page') for team_name in
    team_names
]
urlpatterns.append(path('teams/', views.team_list, name='team_list'))
urlpatterns.append(path('handle-click/', views.handle_click, name='handle_click'),  # Ensure this line is correct
                   )
urlpatterns.append(path('simulate_game/', views.simulate_game, name='simulate_game'),
                   )
