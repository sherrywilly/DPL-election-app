from django.contrib import admin
from election.models import Candidate,Vote
# Register your models here.
admin.site.register(Candidate)
admin.site.register(Vote)