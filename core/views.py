from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout

def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('team_list')
    else:
        return redirect('login')

