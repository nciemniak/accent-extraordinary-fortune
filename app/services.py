from django.conf import settings
import requests

class MyMidjourneyAPI:
  def __init__(self):
    self.api_key = settings.MYMIDJOURNEY_API_KEY
    self.url = "https://api.mymidjourney.ai/api/v1/midjourney/imagine"
    self.headers = {
          "Content-Type": "application/json",
          "Authorization": f"Bearer {self.api_key}",
    }

  def image_to_image(self, zodiac_animal, image_url):
    url = "https://api.mymidjourney.ai/api/v1/midjourney/imagine"
    data = {
      "prompt": f"{image_url} chinese zodiac {zodiac_animal} pixel art character, cute, low res. 8 bit, pixel art, 100% black background --q 0.5"
    }

    try:
      if settings.IMAGE_GENERATION_ON:
        response = requests.post(url, json=data, headers=self.headers)
        response.raise_for_status()
        response_json = response.json()
        message_id = response_json['messageId']
      else:
        # dummy message id
        message_id = '8facad15-0c29-41a2-890c-036546568336'
      
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


class MidjourneyGoAPI:
  def __init__(self):
    self.headers = {
          "X-API-KEY": settings.GOAPI_KEY,
    }

  def image_to_image(self, zodiac_animal, image_url):
    url = "https://api.midjourneyapi.xyz/mj/v2/imagine"
    data = {
      "prompt": f"{image_url} chinese zodiac {zodiac_animal} pixel art character, anthropomorphic, cute, low res. 8 bit, pixel art, 100% black background",
      "aspect_ratio": "1:1",
      "process_mode": "fast",
    }

    response = requests.post(url, headers=self.headers, json=data).json()
    return response['task_id']
  
  def progress(self, task_id):
    url = 'https://api.midjourneyapi.xyz/mj/v2/fetch'
    data = {
      'task_id': task_id
    }

    response = requests.post(url, json=data).json()
    return response

    