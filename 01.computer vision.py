# Computer Vision Object Dectection
# Computer Vision API를 사용해서 이미지속에 있는 사물을 인식하는 데모 입니다.
# 네트워크 통신을 위해서 requests 패키지를 import 합니다.

from symbol import subscript
import requests
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import json

# Subscription Key와 접속에 필요한 URL을 설정합니다.
subscription_key = "PASTE_YOUR_FACE_SUBSCRIPTION_KEY_HERE"
vision_base_url = "https://labuser22computervision.cognitiveservices.azure.com/vision/v2.0/"

analyze_url = vision_base_url + "analyze"

# 분석에 사용되는 이미지를 확인 합니다.
image_url = "https://img.hankyung.com/photo/202101/AA.24972188.1.jpg"

# 이미지를 바이너리로 읽어 con에 저장
con = requests.get(image_url).content
byte = BytesIO(con)
image = Image.open(byte)

headers = {'Ocp-Apim-Subscription-key': subscription_key}
params  = {'visualFeatures': 'Categories,Description,Color'}
data = {'url': image_url}

response = requests.post(analyze_url, headers=headers, params=params,json=data)

result = response.json()

print(result)

image_caption = result["description"]["captions"][0]["text"]

print(image_caption)

objectDetection_url = vision_base_url + 'detect'

image_url = 'https://mblogthumb-phinf.pstatic.net/MjAyMDA5MDdfMjQ1/MDAxNTk5NDY1MjUxMjM4.zbBfDyquP67Utlw2d6pFOtHqnJyfkukH3PTDgDTg8Zkg.qQWiX02sgIaExMrU-guWXKDRsmnGBBxeS_bz2Ioy8YUg.PNG.vet6390/%EA%B0%95%EC%95%84%EC%A7%80_%EA%B3%A0%EC%96%91%EC%9D%B4_%ED%95%A8%EA%BB%98_%ED%82%A4%EC%9A%B0%EA%B8%B0.PNG?type=w800'
image = Image.open(BytesIO(requests.get(image_url).content))

headers = {'Ocp-Apim-Subscription-key': subscription_key}
params  = {'visualFeatures': 'Categories,Description,Color'}
data = {'url': image_url}

response = requests.post(objectDetection_url, headers=headers, params=params,json=data)

result = response.json()

print(result)

draw = ImageDraw.Draw(image)

# boundingBox를 위한 함수
def DrawBox(detectData):
    
    objects = detectData['objects']

    for obj in objects:
        # print(obj)
        rect = obj["rectangle"]
        print(rect)
        
        x = rect["x"]
        y = rect["y"]
        w = rect["w"]
        h = rect["h"]
        
        draw.rectangle(((x,y),(x+w,y+h)), outline="red")
        
        objectName = obj['object']
        draw.text((x,y-10),objectName,fill='red')
        
    
DrawBox(result)

image.show()