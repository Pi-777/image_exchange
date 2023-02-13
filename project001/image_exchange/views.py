# Create your views here.
import os
import base64
from django.shortcuts import render, HttpResponse, redirect
from image_exchange import models
from project001 import settings
from django.core.files.base import ContentFile


def update_info(request):
    if request.method == 'POST':
        new_img = models.Picture(
            image_path=request.FILES.get('photo'),
            name=request.FILES.get('photo').name,
            tag=request.POST.get('tag')
        )
        new_img.save()
        gift_image, tag = read_image()
        return HttpResponse("<html>"
                            "<body>"
                            "<img src='data:image/jpeg;base64,{}' width='700' height='500'>"
                            "<br><p>{}</p>"
                            "</body>"
                            "</html>"
                            .format(base64.b64encode(gift_image).decode('utf-8'), tag))
    return render(request, 'display.html')


def random_image_info():
    import random
    import sqlite3

    # Connect to the database
    conn = sqlite3.connect("image_data")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM image_exchange_picture")
    total_images = cursor.fetchone()[0]

    random_index = random.randint(1, total_images)
    cursor.execute("SELECT * FROM image_exchange_picture WHERE id=?", (random_index,))
    random_image = cursor.fetchone()

    conn.close()

    return random_image


def read_image():
    try:
        image = random_image_info()
        file_name = image[1]
        file_tag = image[3]
        image_path = os.path.join(settings.BASE_DIR, "media/{}".format(file_name))
        with open(image_path, 'rb') as f:
            image_data = f.read()
        # return HttpResponse(image_data, content_type="image/png")
        return image_data, file_tag
    except Exception as e:
        print(e)
        return HttpResponse(str(e)), HttpResponse(str(e))
