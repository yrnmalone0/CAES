from django.shortcuts import render
from job.models import Job, ApplyJob

def home(request):
    return render(request, 'frontend/home.html')


#Job Listing
def job_listing(request):
    jobs = Job.objects.filter(is_available=True).order_by('-timestamp')
    context = {'jobs':jobs}
    return render(request, 'frontend/job_listing.html', context)


#View Job Details
def job_details(request, pk):
    if ApplyJob.objects.filter(user=request.user, job=pk).exists():
        has_applied = True
    else:
         has_applied = False
    job = Job.objects.get(pk=pk)
    context = {'job':job, 'has_applied':has_applied}
    return render(request, 'frontend/job_details.html', context)