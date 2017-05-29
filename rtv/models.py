from django.db import models
from django.core.urlresolvers import reverse

class Report(models.Model):
    topic = models.CharField(max_length = 100)
    license_plate = models.CharField(max_length = 30)
    address = models.CharField(max_length = 100)
    date = models.DateTimeField(blank = False)
    image = models.FileField()


    def get_absolute_url(self):
        return reverse('rtv:detail', kwargs = {'pk':self.pk})

    def __str__(self):
        return self.topic + ' - ' + self.license_plate

class order(models.Model):
    report = models.ForeignKey(Report, on_delete = models.CASCADE)
