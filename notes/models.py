from datetime import datetime
from django.db import models
from base.models import departments, Teachers


class Note(models.Model):
    subject = models.CharField(max_length=40, choices=departments, default="Others")
    topic = models.CharField(max_length=200, blank=True)
    publication_date = models.DateField(default=datetime.now)
    teacher = models.ForeignKey(Teachers)
    note = models.FileField(upload_to="./notes/files")

    def __str__(self):
        return "Notes by {}".format(str(self.teacher))