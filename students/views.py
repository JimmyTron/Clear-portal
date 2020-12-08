from django.shortcuts import render, get_object_or_404
from .models import StudentProfile, Clearance
from django.views import View
# Create your views here.

def clearance(request):
    profile = StudentProfile.objects.filter(user=request.user).first()
    clearance = Clearance.objects.filter(cleared=False,student=profile)
    context = {
        'clearance': clearance, 
        'title': 'Clearance',
    }
    return render(request, "clearance.html", context)

class profile(View):
    pass

