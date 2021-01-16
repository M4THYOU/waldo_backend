from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import WaldoGameForm
from .models import WaldoGame

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


def success(request):
    return HttpResponse('successfully uploaded')


def display_waldo_images(request):
    waldos = WaldoGame.objects.all()
    return render(request, 'display_waldo_images.html', {'waldo_imgs': waldos})
