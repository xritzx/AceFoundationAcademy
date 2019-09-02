from datetime import datetime
from django.db import models

EXAM_TYPES=(
    ('Weekly Test', 'Weekly Test'),
    ('Evaluation Test', 'Evaluation Test'),
)

class Exam(models.Model):
    exam_name = models.CharField(max_length=300)
    exam_type = models.CharField(max_length=100)
    exam_date = models.DateTimeField(verbose_name="Date of Exam", default=datetime.now)