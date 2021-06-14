from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from demoapp.forms import SignupForm
from django.http import HttpResponseRedirect

# Create your views here.
def homepage_view(request):
    return render(request,'demoapp/home.html')

@login_required
def diet_view(request):
    return render(request,'demoapp/DietPlan.html')

@login_required
def entertainment_view(request):
    return render(request,'demoapp/Entertainment.html')

@login_required
def exercise_view(request):
    return render(request,'demoapp/Exercises.html')

@login_required
def doctor_view(request):
    return render(request,'demoapp/Doctors.html')

def logout_view(request):
    return render(request,'demoapp/logout.html')

def signup_view(request):
    form = SignupForm()
    if request.method=='POST':
      form=SignupForm(request.POST)
      if form.is_valid():
        form.save()
      return HttpResponseRedirect('/accounts/login/')
    return render(request,'demoapp/signup.html',{'form':form})
