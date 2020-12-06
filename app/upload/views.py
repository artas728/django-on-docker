from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from .models import TestModel
import json
import redis
import time

redis_cli = redis.Redis(host='127.0.0.1', port=6379, db=0)

def save_to_redis(request):
    data = json.loads(request.body.decode())
    for key, value in data.items():
        redis_cli.rpush(key, value)
    return JsonResponse({'success': True, 'data': 'Saved in Redis'})

def endpoint(request):
    time.sleep(1)
    return JsonResponse({'success': True, 'data': 'Request processed'})

def write_to_db(request):
    data = json.loads(request.body.decode())
    for row in data:
        TestModel.objects.create(key1=row['key1'],
                                 key2=row['key2'],
                                 key3=row['key3'],
                                 key4=row['key4'])
    return JsonResponse({'success': True, 'data': 'Data has been saved'})

def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload.html", {
            "image_url": image_url
        })
    return render(request, "upload.html")
