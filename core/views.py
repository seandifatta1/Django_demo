from django.shortcuts import redirect

def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('team_list')
    else:
        return redirect('login')
