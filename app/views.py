from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils.dateparse import parse_date

from datetime import datetime

from .models import Zodiac

# testing
import pdb
# end testing

def index(request):
    context = { "test": "test text" }
    return render(request, "app/index.html", context)


def zodiac(request):
    birthday = request.POST["birthday"]
    birthday_parsed = parse_date(birthday)
    
    zodiac = Zodiac.objects.filter(start_date__lte=birthday_parsed, end_date__gte=birthday_parsed).first()
    return render(request, "app/zodiac.html", {"zodiac": zodiac})
