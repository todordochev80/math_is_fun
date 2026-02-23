from django.db import models

from exercises.models import OperationChoices


class Star(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_css = models.CharField(max_length=50, default="fa-star")

    def __str__(self):
        return self.title

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    badges = models.ManyToManyField(Star, blank=True, related_name='children')

    def __str__(self):
        return self.name



class Score(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='scores')
    score = models.IntegerField(null=True, blank=True)
    date_achieved = models.DateTimeField(auto_now_add=True)
    operation_type = models.CharField(max_length=20, choices=OperationChoices.choices)

    def __str__(self):
        return f"{self.player.name} - {self.score}"

    class Meta:
        ordering = ['-score']



