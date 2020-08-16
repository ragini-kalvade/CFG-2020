from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def indexview(request):
    return render(request,'index.hml')

@login_required
def dashboardview(request):
    return render(request,'dashboardview.html')

def registerview(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registeration/register.html',{'form':form})
