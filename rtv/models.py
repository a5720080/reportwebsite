from django.db import models

class Report(models.Model):
    topic = models.CharField(max_length = 100)
    license_plate = models.CharField(max_length = 10)
    address = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now = True , blank = False)

class order(models.Model):
    report = models.ForeignKey(Report, on_delete = models.CASCADE)
