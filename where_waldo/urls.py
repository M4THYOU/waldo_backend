from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('success', views.success, name='success'),
    path('waldo_images', views.display_waldo_images, name='display_waldo_images')
]
