from django.db import models

# Create your models here.

class Square(models.Model):
    vertical_id = models.IntegerField(blank=False)
    horizontal_id = models.IntegerField(blank=False)
    owner = models.ForeignKey('UserProfile', on_delete=models.SET_NULL)


class UserProfile(models.Model):
    color = models.CharField(max_length=15, blank=False)
    user_id = models.CharField(max_length=50, blank=False, primary_key=True)

    def get_user_score(self):
        return Square.objects.count(owner=self)