from datetime import datetime
from django.db import models
from base.models import departments, Teachers


class Note(models.Model):
    subject = models.CharField(max_length=40, choices=departments, default="Others")
    topic = models.CharField(max_length=200, blank=True)
    publication_date = models.DateField(default=datetime.now)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    note = models.FileField(upload_to="notes/", null=True, blank=True)
    for_class = models.IntegerField(max_length=50, default=10)

    def __str__(self):
        return "Notes by {} for {} on {}".format(str(self.teacher), str(self.for_class), str(self.topic))