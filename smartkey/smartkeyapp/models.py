from django.db import models
from django.utils import timezone

class Distance(models.Model):
    class Meta:
        db_table="distance"
        verbose_name="距離"

    length = models.Floatfield(verbose_name="距離")
    measured_time = models.DateTimeField(verbose_name="計測日時", default=timezone.now)