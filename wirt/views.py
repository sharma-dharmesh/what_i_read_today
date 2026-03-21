from django.shortcuts import render

def index(request):
    """The home page for wirt"""
    return render(request, 'wirt_pages/index.html')