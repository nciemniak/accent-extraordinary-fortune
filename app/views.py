from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils.dateparse import parse_date

from datetime import datetime

from .models import Zodiac
from .forms import ImageForm

# testing
import pdb
# end testing

def index(request):
  context = { "test": "test text" }
  return render(request, "app/index.html")


def zodiac(request):
  birthday = request.POST.get("birthday", None)

  if birthday is None:
    zodiac_id = request.GET.get("zodiac_id", None)
    zodiac = get_object_or_404(Zodiac, pk=zodiac_id)
  else:
    birthday_parsed = parse_date(birthday)
    zodiac = Zodiac.objects.filter(start_date__lte=birthday_parsed, end_date__gte=birthday_parsed).first()
    
  all_zodiacs = Zodiac.objects.all()
  return render(request, "app/zodiac.html", {"zodiac": zodiac, "all_zodiacs": all_zodiacs, "show_navbar": True })


def upload_selfie(request):
  if request.method == 'POST':
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()

  zodiac_id = request.GET.get("zodiac_id", None)
  form = ImageForm()

  return render(request, "app/upload_selfie.html", { "show_navbar": True, "zodiac_id": zodiac_id, "form": form })


def result(request):
  if request.method == 'POST':
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()