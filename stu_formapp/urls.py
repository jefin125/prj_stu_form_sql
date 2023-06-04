from django.contrib import admin
from django.urls import path
from stu_formapp import views

urlpatterns = [
    path('admin',admin.site.urls),
    path('index',views.index),
]