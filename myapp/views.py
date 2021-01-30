from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Student
from .models import Student



# Create your views here.
def home(request):
    # return HttpResponse("xây dựng truy xuất dữ liệu đến sqllite")

     rs = Student.objects.all()
     content = {
        'rs': rs,
     }
     return render(request,'pages/home.html', content)
