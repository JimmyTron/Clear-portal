from django.shortcuts import render, get_object_or_404
from .models import StudentProfile, Clearance
# Create your views here.

def profile(request):
    profile = StudentProfile.objects.filter(user=request.user).first()
    clearance = Clearance.objects.filter(is_cleared=False,student=profile)
    context = {'clearance': clearance}
    return render(request, "profile.html",context)
