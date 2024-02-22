from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

# testing
import pdb
# end testing

def index(request):
    context = { "test": "test text" }
    return render(request, "app/index.html", context)


def zodiac_animal(request):
    birthday = request.POST["birthday"]
    breakpoint()

    context = { "test": "test text" }
    return render(request, "app/zodiac_animal.html", context)
