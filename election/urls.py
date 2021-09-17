from django.urls import path
from election.views import LeaderBoard, CandidateList, make_votes

urlpatterns = [
    path('leaderboard/', LeaderBoard, name="leaderboard"),
    path('candidates/', CandidateList, name="candidates"),
    path('vote/', make_votes, name="vote"),

]
