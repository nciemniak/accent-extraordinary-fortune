from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils.dateparse import parse_date

from .services import MyMidjourneyAPI, MidjourneyGoAPI
from .constants import FORTUNES

from datetime import datetime
import json
import random

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
  zodiac_id = request.GET.get("zodiac_id", None)

  return render(request, "app/upload_selfie.html", { "show_navbar": True, "zodiac_id": zodiac_id })


def result(request):
  if request.method == 'POST':
    zodiac_id = request.POST.get("zodiac_id", None)
    zodiac = get_object_or_404(Zodiac, pk=zodiac_id)
    image_url = request.POST.get("uploaded_image_url", None)

    # MyMidjourney
    # mymidjourney_api = MyMidjourneyAPI()
    # message_id = mymidjourney_api.image_to_image(zodiac.animal, image_url)

    # GoAPI
    go_api = MidjourneyGoAPI()
    message_id = go_api.image_to_image(zodiac.animal, image_url)

    context = {
      "show_navbar": True, 
      "message_id": message_id, 
      "zodiac": zodiac, 
      "fortune": _get_random_fortune,
      "image_url": image_url,
    }
    return render(request, "app/result.html", context)
  
  elif request.method == 'GET':
    fortune = _get_random_fortune()
    return render(request, "app/result.html", { "show_navbar": True, 'message_id': 111, "fortune": _get_random_fortune })


def midjourney_task_progress(request):
  message_id = request.GET.get("message_id", None)

  # mymidjourney_api = MyMidjourneyAPI()
  # data = mymidjourney_api.progress(message_id)
  
  go_api = MidjourneyGoAPI()
  data = go_api.progress(message_id)

  return JsonResponse(data)


def _get_random_fortune():
  fortunes_list = FORTUNES
  fortune_number = random.randint(1, 88)

  result = next(
     (obj for obj in fortunes_list if obj["number"] == fortune_number), None
  )
  return result['luck']