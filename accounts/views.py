from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect
from django.urls import reverse
from election.decorators import unauth_user

User = get_user_model()

def error_404_view(request, exception):
    return render(request,'error_404.html')
@unauth_user
def userLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        dob = request.POST.get('password')
        user = User.objects.filter(email=email, dob=dob)
        if user:
            login(request, user[0])
            if user[0].vote_set.all().exists():
                return redirect(reverse('leaderboard'))
            return redirect(reverse('candidates'))
        messages.error(request, 'Invalid credentials.')
    return render(request, "accounts/registration.html")
