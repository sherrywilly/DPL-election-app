import json

from django.db import transaction
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from election.decorators import auth_user
from election.models import Vote, Candidate


def LeaderBoard(request):
    leadershipbyvotes = Candidate.objects.annotate(count=Count('votes__id')).order_by('-count')[:4]
    context = {
        "leadershipbyvotes": leadershipbyvotes
    }
    return render(request, "election/leadership.html", context)


@csrf_exempt
def make_votes(request):
    if request.user.vote_set.all().exists():
        return JsonResponse({"status": "already voted user"})
    if request.method == "POST":
        list = request.POST.getlist('arr[]')
        with transaction.atomic():
            for i in list:
                vote = Vote()
                vote.candidate_id = i
                vote.voter = request.user
                vote.save()
            return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'Fail', 'message': "something went wrong"})


@auth_user
def CandidateList(request):
    context = {
        "candidates": Candidate.objects.all()
    }
    return render(request, "election/candidate.html", context)
