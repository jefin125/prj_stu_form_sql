from django.shortcuts import render
from . forms import EmpForm

def index(request):
    stu = EmpForm()
    return render(request,"index.html",{'form':stu})

# Create your views here.
