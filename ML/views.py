from django.http import JsonResponse, HttpResponse, Http404
from PIL import Image
import json
import torch
from Image.models import ImageFile
from Image.serializers import ImageFileSerializer, DetectedImageFileSerializer
from Solutions.models import Code
from Solutions.serializers import CodeSerializer
from Accounts.models import User
from Posts.models import Post
from Posts.serializers import PostSerializer
import requests
import requests

def run(request):
    model = torch.hub.load('yolov5', 'custom', path='model_best.pt', source='local')

    username = request.GET.get('firmUser')
    print('user->', username)
    user = User.objects.filter(email=username).values('id')
    userinfo = User.objects.get(email=username)

    img_url = ImageFile.objects.filter(user__in=user)
    img_serializers = ImageFileSerializer(img_url, many=True)
    

    ## crop mmclassification Test Code
    # file = {'input':open(img_serializers.data[0]['image'][1:], 'rb')}

    # response = requests.post('http://211.184.190.112:8001/crop_mmclassification/', files=file)
    # data = response.json()
    # print('response-> ', data['crop_id'])
    # crop_id = data['crop_id']
    crop_id = 1
    
    img = Image.open(img_serializers.data[0]['image'][1:])
    
    results = model(img)
    results.render()
    
    
    # 클래스 별로 솔루션 제공해서 보내기
    json_rst = json.loads(results.pandas().xyxy[0].to_json(orient='index'))
    print(json_rst)
    if not json_rst:
        raise Http404('Detected Nothing')
    else:
        # detected img 저장
        for img in results.ims:
            Image.fromarray(img).save('./media/detected/detected_'+ img_serializers.data[0]['image'].split('/')[-1])

        nearest = None

        for i in range(len(json_rst)):
            class_id = json_rst[str(i)]['class']
            
            # solution_id = Solutions.objects.filter(solution_id=class_id)
            # solution_serializer = SolutionsSerializer(solution_id, many=True)
            # # print('solution_serializer.data-> ', solution_serializer.data)
            # json_rst[str(i)]['solution_default'] = solution_serializer.data[0]['solution_default']
        print(class_id)
        code = Code.objects.filter(dist_id=class_id).filter(crop_id=crop_id)
        code = CodeSerializer(code, many=True).data[0]['id']

        # detected_image save
        detected_image_url = 'detected/detected_' + img_serializers.data[0]['image'].split('/')[-1]
        detected_class_id = code
        data = {
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
    response = requests.post('http://127.0.0.1:8000/similarity/', files=files)

    return HttpResponse(response)

def deep_ranking(request):
    detected_url = DetectedImageFile.objects.all()
    count = DetectedImageFile.objects.count()
    detected_serializers = DetectedImageFileSerializer(detected_url, many=True)

    files = []
    for i in range(1, count):
        files.append(('files',open(detected_serializers.data[i]['image'].lstrip('/'), 'rb')))
        print(detected_serializers.data[i]['image'].lstrip('/'))
    files.append(('input_file',open(detected_serializers.data[0]['image'].lstrip('/'), 'rb')))
    response = requests.post('http://127.0.0.1:8002/similarity/', files=files)
    response_json = response.json()
    data = {}

    localhost = 'http://127.0.0.1:8000/'
    for i in range(1, 4):
        detected_image_name = localhost + response_json['rank'+str(i)]
        post = Post.objects.filter(is_public=True).filter(detected_image=detected_image_name)
        post_serializers = PostSerializer(post)
        print(post_serializers)
        data['rank'+str(i)] = post_serializers.data
        print(data['rank'+str(i)])

    print(data)
    return HttpResponse(data)