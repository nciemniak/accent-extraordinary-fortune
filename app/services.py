from django.conf import settings
import requests
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class MyMidjourneyAPI:
  def __init__(self):
    self.api_key = settings.MYMIDJOURNEY_API_KEY
    self.url = "https://api.mymidjourney.ai/api/v1/midjourney/imagine"
    self.headers = {
          "Content-Type": "application/json",
          "Authorization": f"Bearer {self.api_key}",
    }

  def image_to_image(self):
    url = "https://api.mymidjourney.ai/api/v1/midjourney/imagine"
    data = {
      "prompt": "https://media.newyorker.com/photos/5909744ec14b3c606c1085ad/master/w_2560%2Cc_limit/040823_r13315.jpg <object/character> chinese zodiac dragon pixel art character, cute, low res. 8 bit, pixel art, 100% black background --q 0.5"
    }

    try:
      breakpoint()
      response = requests.post(url, json=data, headers=self.headers)
      response.raise_for_status()
      response_json = response.json()
      message_id = response_json['messageId']
      return message_id
    except requests.exceptions.RequestException as e:
      # Handle any exceptions (e.g., connection error, timeout)
      print(f"Error: {e}")
      return None

  def progress(self, message_id):
    url = f"https://api.mymidjourney.ai/api/v1/midjourney/message/{message_id}"

    try:
      response = requests.get(url, headers=self.headers)
      return response.json()
    except requests.exceptions.RequestException as e:
      print(f"Error: {e}")
      return None