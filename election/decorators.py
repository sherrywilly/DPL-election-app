from django.shortcuts import redirect
from django.urls import reverse


def unauth_user(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect(reverse('candidates'))

    return wrapper

def auth_user(view_func):
    def wrapper(request, *args, **kwargs):
        if  request.user.is_authenticated:
            if request.user.is_eligible:
                return view_func(request, *args, **kwargs)
            return redirect(reverse('leaderboard'))

        else:
            return redirect(reverse('user-login'))

    return wrapper