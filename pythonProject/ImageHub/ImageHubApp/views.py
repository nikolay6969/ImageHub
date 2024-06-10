from django.shortcuts import render
from .models import Images
def index(request):

    imagesBD = {
        'images': Images.objects.all()
    }

    return render(request, "index.html", imagesBD)
# Create your views here.
