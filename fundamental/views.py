from django.shortcuts import render

from fundamental.models import All_Photos

# Create your views here.

def index(request):
    bihar_photos = All_Photos.objects.all()
    return render(request, "index.html", {'bihar_photos':bihar_photos})