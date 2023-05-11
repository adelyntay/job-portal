from django import forms


# create listing form class
class JobListing(forms.Form):
    job_title = forms.CharField(max_length=80)
    company = forms.CharField(max_length=80)
    description = forms.CharField(max_length=80)
    requirements = forms.CharField(max_length=80)
    salary = forms.DecimalField(max_digits=10, decimal_places=2)
    date_posted = forms.DateField()