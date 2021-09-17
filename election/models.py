from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from versatileimagefield.fields import PPOIField, VersatileImageField

User = get_user_model()

class Candidate(models.Model):
    name = models.CharField(verbose_name="Full name",max_length=100)
    image = VersatileImageField(upload_to="candidates", ppoi_field="ppoi", blank=False)
    ppoi = PPOIField()
    desg = models.CharField(max_length=100,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.name

    @property
    def first_name(self):
        try:
            name = self.name.split()
            name = name[0]
        except IndexError:
            name = None
        return name
    @property
    def get_image_url(self):
        try:
            url = self.image.crop['640x640'].url
        except:
            url = ''
        return url
    @property
    def count_vote(self):
        try:
            count = len(self.votes.all())
        except:
            count = 0
        return count
    @property
    def get_small_img_url(self):
        try:
            url = self.image.crop['242x242'].url
        except:
            url = ''
        return url


class Vote(models.Model):
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE,related_name="votes")
    voter = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('candidate','voter',)


