from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addbasvuru/<int:id>', views.addbasvuru, name='addbasvuru'),
]