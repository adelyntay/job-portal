from django.shortcuts import render
from .listings import JobListing
from .models import Job
from django.contrib import messages


# Create your views here.
def posting(request):
    if request.method == "POST":
        form = JobListing(request.POST)
        if form.is_valid():
            job_title = form.cleaned_data["job_title"]
            company = form.cleaned_data["company"]
            description = form.cleaned_data["description"]
            requirements = form.cleaned_data["requirements"]
            salary = form.cleaned_data["salary"]
            date_posted = form.cleaned_data["date_posted"]

            Job.objects.create(job_title=job_title, company=company,
                               description=description, requirements=requirements,
                               salary=salary, date_posted=date_posted)

            messages.success(request, "Job listing successfully created")
    return render(request, "listing.html")