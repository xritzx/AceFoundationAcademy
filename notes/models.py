from datetime import datetime
from django.db import models
from base.models import departments, Teachers


class Note(models.Model):
    subject = models.CharField(max_length=40, choices=departments, default="Others")
    topic = models.CharField(max_length=200, blank=True)
    publication_date = models.DateField(default=datetime.now)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    note = models.URLField(max_length=2000, help_text="Please Enter the URL here(GDrive/Amazon Drive)", default="/")
    for_class = models.IntegerField(default=6, help_text="For global notice put class=69")

    def __str__(self):
        return "Notes by {} for {} on {}".format(str(self.teacher), str(self.for_class), str(self.topic))