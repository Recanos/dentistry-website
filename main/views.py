from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def specialist(request):
    return render(request, 'teeth/specialist.html')