from django.db import models

# Create your models here.
from django.utils import timezone

class Distance(models.Model):
    class Meta:
        db_table="distance"
        verbose_name="距離"
        verbose_name_plural="距離"

    date = models.DateTimeField(verbose_name="時刻", default=timezone.now)
    distance = models.FloatField(verbose_name="距離")
    source = models.CharField(verbose_name="ソース", max_length=20,null=True)

    def __str__(self):
        s = "date:{}, distance:{}, source:{}".format(datetime.strftime(self.date, "%Y-%m-%d"), self.distance, self.source)

        return s
