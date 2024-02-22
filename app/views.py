from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

def index(request):
    context = { "test": "test text" }
    return render(request, "app/index.html", context)
    #return HttpResponse("Hello, world. You're at the polls index.")
