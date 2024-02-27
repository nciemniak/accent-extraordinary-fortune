from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils.dateparse import parse_date
from .services import MyMidjourneyAPI

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
    zodiac_id = request.POST.get("zodiac_id", None)

    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        
        # Initialize the MyMidjourneyImageToImageAPI service
        mymidjourney_api = MyMidjourneyAPI()
        # Perform image transformation
        message_id = mymidjourney_api.image_to_image()

        return render(request, "app/result.html", { "show_navbar": True, "message_id": message_id, "zodiac_id": zodiac_id })
  elif request.method == 'GET':
    return render(request, "app/result.html", { "show_navbar": True, 'message_id': 111 })


def midjourney_task_progress(request):
  message_id = request.GET.get("message_id", None)

  mymidjourney_api = MyMidjourneyAPI()
  data = mymidjourney_api.progress(message_id)
  return JsonResponse(data)


def test_view(request):
  return render(request, "app/test.html")