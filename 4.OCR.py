from urllib import response
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# Azure Key-Vault를 사용하면 암호화할 수 있음
subscription_key = '****************'
vision_base_url = '*********************'
ocr_url = vision_base_url + 'ocr'

image_url = 'https://i.stack.imgur.com/WiDpa.jpg'

image = Image.open(BytesIO(requests.get(image_url).content))

headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {'language': 'unk', 'detectOrientation': 'true'}
data = {'url': image_url}

response = requests.post(ocr_url, headers=headers, params=params, json=data)

result = response.json()
print(result)

for region in result['regions']:
  lines = region['lines']

  for line in lines:
    words = line['words']

    for word in words:
      print(word['text'])
      
image_url = "https://www.unikorea.go.kr/unikorea/common/images/content/peace.png"
image = Image.open(BytesIO(requests.get(image_url).content))

headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {'language': 'ko', 'detectOrientation': 'true'}
data = {'url': image_url}

response = requests.post(ocr_url, headers=headers, params=params, json=data)
result = response.json()
print(result)

for region in result['regions']:
  lines = region['lines']

  for line in lines:
    words = line['words']

    for word in words:
      print(word['text'])