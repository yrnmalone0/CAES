from django.shortcuts import render
from job.models import Job

def home(request):
    return render(request, 'frontend/home.html')


#Job Listing
def job_listing(request):
    jobs = Job.objects.filter(is_available=True)
    context = {'jobs':jobs}
    return render(request, 'frontend/job_listing.html', context)


#View Details
def job_details(request, pk):
    job = Job.objects.get(pk=pk)
    context = {'job':job}
    return render(request, 'frontend/job_details.html', context)