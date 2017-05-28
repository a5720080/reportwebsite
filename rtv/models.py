from django.db import models

class Report(models.Model):
    topic = models.CharField(max_length = 100)
    license_plate = models.CharField(max_length = 30)
    address = models.CharField(max_length = 100)
    date = models.DateTimeField(blank = False)


    def __str__(self):
        return self.topic + ' - ' + self.license_plate

class order(models.Model):
    report = models.ForeignKey(Report, on_delete = models.CASCADE)
