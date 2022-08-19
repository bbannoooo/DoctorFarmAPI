from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from tensorflow import keras
from keras.models import load_model
from PIL import Image
import numpy as np
import json
import torch
import pandas
from Image.models import ImageFile
from Image.serializers import ImageFileSerializer
from Solutions.models import Solutions
from Solutions.serializers import SolutionsSerializer

def run(request):
    model = torch.hub.load('yolov5_code', 'custom', path='model_best.pt', source='local')

    user = request.user
    img_url = ImageFile.objects.filter(email=user)
    img_serializers = ImageFileSerializer(img_url, many=True)
    # print(img_serializers.data[0]['image'])

    img = Image.open(img_serializers.data[0]['image'][1:])
    results = model(img)
    results.render()
    for img in results.imgs:
        Image.fromarray(img).save('./media/detected/detected_'+ img_serializers.data[0]['image'].split('/')[-1])
    detected_img = '../media/detected/detected_' + img_serializers.data[0]['image'].split('/')[-1]
    # print(detected_image)
    # print(type(detected_image))
    # print('results -> ', results)
    # print('results.pandas().xyxy[0]-> ', results.pandas().xyxy[0])
    # print('json_rst-> ', json_rst)

    # 클래스 별로 솔루션 제공해서 보내기
    json_rst = json.loads(results.pandas().xyxy[0].to_json(orient='index'))
    
    for i in range(len(json_rst)):
        class_id = json_rst[str(i)]['class']
        solution_id = Solutions.objects.filter(solution_id=class_id)
        solution_serializer = SolutionsSerializer(solution_id, many=True)
        json_rst[str(i)]['solution_default'] = solution_serializer.data[0]['solution_default']
    json_rst['detected_image'] = detected_img
    
    # return HttpResponse(f'<img src={imgtitle}/>')
    # return JsonResponse(img_serializers.data[0]['image'], safe=False)
    return JsonResponse(json_rst)
