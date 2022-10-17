# pip install azure-cognitiveservices-vision-customvision
# https://learn.microsoft.com/ko-kr/azure/cognitive-services/Custom-Vision-Service/quickstarts/image-classification?tabs=visual-studio&pivots=programming-language-python#train-the-project
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

# 클라이언트 인증
ENDPOINT = "PASTE_YOUR_CUSTOM_VISION_TRAINING_ENDPOINT_HERE"
training_key = "PASTE_YOUR_CUSTOM_VISION_TRAINING_SUBSCRIPTION_KEY_HERE"
prediction_key = "PASTE_YOUR_CUSTOM_VISION_PREDICTION_SUBSCRIPTION_KEY_HERE"
prediction_resource_id = "PASTE_YOUR_CUSTOM_VISION_PREDICTION_RESOURCE_ID_HERE"

publish_iteration_name = "classifyModel"

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

# 새 Custom Vision 프로젝트 만들기
print ("Creating project...")
project = trainer.create_project("Labuser22 Project")

# 프로젝트에 태그 추가
Jajangmyeon_tag = trainer.create_tag(project.id, "Jajangmyeon")
Champon_tag = trainer.create_tag(project.id, "Champon")
Tangsuyug_tag = trainer.create_tag(project.id, "Tangsuyug")

# 이미지 업로드 및 태그 지정

base_image_location = os.path.join (os.path.dirname(__file__), "Images")
print("Adding images...")

image_list = []
for image_num in range(1, 21):
    file_name = "{}.jpg".format(image_num)
    with open(os.path.join (base_image_location, "Jajangmyeon", file_name), "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[Jajangmyeon_tag.id]))
for image_num in range(1, 21):
    file_name = "{}.jpg".format(image_num)
    with open(os.path.join (base_image_location, "Champon", file_name), "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[Champon_tag.id]))
for image_num in range(1, 21):
    file_name = "{}.jpg".format(image_num)
    with open(os.path.join (base_image_location, "Tangsuyug", file_name), "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[Tangsuyug_tag.id]))        
upload_result = trainer.create_images_from_files(project.id, ImageFileCreateBatch(images=image_list))

if not upload_result.is_batch_successful:
    print("Image batch upload failed.")
    for image in upload_result.images:
        print("Image status: ", image.status)
    exit(-1)

# 프로젝트 학습
print('Training....')
iteration = trainer.train_project(project.id)
while (iteration.status != 'Completed'):
  iteration = trainer.get_iteration(project.id, iteration.id)
  print('Training status' + iteration.status)

  time.sleep(3)

print('Done!')

# 예측 엔드포인트 테스트
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

base_image_location = os.path.join (os.path.dirname(__file__), "Images")
with open(os.path.join (base_image_location, "Test/test_image.jpg"), "rb") as image_contents:
    results = predictor.classify_image(
        project.id, publish_iteration_name, image_contents.read())

    # 출력
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))