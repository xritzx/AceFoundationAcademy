from datetime import datetime
from django.db import models

EXAM_TYPES=(
    ('JEE MAINS', 'JEE MAINS'),
    ('JEE ADVANCED', 'JEE ADVANCED'),
    ('NEET', 'NEET'),
    ('AIIMS', 'AIIMS'),
    ('WBJEE', 'WBJEE'),
)

class Exam(models.Model):
    exam_name = models.CharField(max_length=300)
    exam_type = models.CharField(max_length=100)
    exam_date = models.DateTimeField(verbose_name="Date of Exam", default=datetime.now)