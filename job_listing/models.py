from django.db import models


# Create your models here.
class Job(models.Model):
    job_title = models.CharField(max_length=80)
    company = models.CharField(max_length=80)
    description = models.CharField(max_length=80)
    requirements = models.CharField(max_length=80)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_posted = models.DateField()