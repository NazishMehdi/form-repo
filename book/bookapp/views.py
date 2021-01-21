from django.shortcuts import render
from bookapp.models import Book
# Create your views here.
def view1(request):
    b=Book.objects.all()
    d={'bk':b}
    return render(request,'bookapp/1.html',d)
