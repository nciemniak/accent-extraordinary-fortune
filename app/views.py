from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

# testing
import pdb
# end testing

def index(request):
    context = { "test": "test text" }
    return render(request, "app/index.html", context)


def zodiac(request):
    birthday = request.POST["birthday"]

    context = { "test": "test text" }
    return render(request, "app/zodiac.html", context)
