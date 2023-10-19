from django.contrib import admin
from django.urls import path
from HW22 import views as HW22_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HW22_views.index, name='index'),
]
