from django.http import JsonResponse, HttpResponse
from PIL import Image
import json
import torch
from Image.models import ImageFile
from Image.serializers import ImageFileSerializer, DetectedImageFileSerializer
from Solutions.models import Solutions
from Solutions.serializers import SolutionsSerializer
from Accounts.models import User
import requests

def run(request):
    model = torch.hub.load('yolov5', 'custom', path='model_best.pt', source='local')

    username = request.GET.get('firmUser')
    print('user->', username)
    user = User.objects.filter(email=username).values('id')
    userinfo = User.objects.get(email=username)

    img_url = ImageFile.objects.filter(user__in=user)
    img_serializers = ImageFileSerializer(img_url, many=True)
    img = Image.open(img_serializers.data[0]['image'][1:])
    results = model(img)
    results.render()
    # detected img 저장
    for img in results.ims:
        Image.fromarray(img).save('./media/detected/detected_'+ img_serializers.data[0]['image'].split('/')[-1])
    
    # 클래스 별로 솔루션 제공해서 보내기
    json_rst = json.loads(results.pandas().xyxy[0].to_json(orient='index'))
    print(json_rst)
    for i in range(len(json_rst)):
        class_id = json_rst[str(i)]['class']
        solution_id = Solutions.objects.filter(solution_id=class_id)
        solution_serializer = SolutionsSerializer(solution_id, many=True)
        print('solution_serializer.data-> ', solution_serializer.data)
        json_rst[str(i)]['solution_default'] = solution_serializer.data[0]['solution_default']
    
    # detected_image save
    detected_image_url = 'detected/detected_' + img_serializers.data[0]['image'].split('/')[-1]
    detected_class_id = class_id
    data = {
        # 'email': str(user),
        'class_id': detected_class_id,
    }
    
    detected_object_serializer = DetectedImageFileSerializer(data=data)
    detected_object_serializer.is_valid(raise_exception=True)
    detected_object_serializer.save(image=detected_image_url, user=userinfo)

    return JsonResponse(json_rst)

def test(request):
    img_url = ImageFile.objects.all()
    img_serializers = ImageFileSerializer(img_url, many=True)

    files = (('input',open(img_serializers.data[3]['image'].lstrip('/'), 'rb')),('files',(open(img_serializers.data[0]['image'].lstrip('/'), 'rb'))) ,('files',(open(img_serializers.data[1]['image'].lstrip('/'), 'rb'))))

    # files2 = {
    #     'input': open(img_serializers.data[0]['image'].lstrip('/'), 'rb'),
    #     'files': files
    # }
    # print(files2['files'])

    response = requests.post('http://127.0.0.1:8000/similarity/', files=files)

    return HttpResponse(response)