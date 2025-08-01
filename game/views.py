from django.shortcuts import render

def home(request):
    return render(request, 'game/index.html')  # make sure the template exists
