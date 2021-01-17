from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from os.path import basename
from os import environ

from .forms import WaldoGameForm
from .models import WaldoGame

from run_inference import inference

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = WaldoGameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = WaldoGameForm()
    return render(request, 'image_form.html', {'form': form})


def upload(request):
    if request.method == 'POST':
        form = WaldoGameForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()

            img_root = settings.MEDIA_ROOT + '/images/'
            img_url = photo.img.url
            img_name = basename(img_url)

            inference(img_root + img_name, img_root)
            photo.result_img = 'images/predicted-' + img_name
            photo.save()

            data = {'is_valid': True, 'name': 'no_name', 'url': img_url, 'predicted_url': photo.result_img.url}
        else:
            data = {'is_valid': False}

        return JsonResponse(data)


def success(request):
    # image_root = settings.MEDIA_ROOT + '/images/'
    # inference(image_root + '1.jpg', image_root)
    print(environ['S3_BUCKET_NAME'])
    return HttpResponse('successfully uploaded')


def display_waldo_images(request):
    waldos = WaldoGame.objects.all()
    return render(request, 'display_waldo_images.html', {'waldo_imgs': waldos})
