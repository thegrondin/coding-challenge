from django.contrib import admin
from django.urls import path

from ninjify.models import *
from ninjify.views import NinjifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ninjify/', NinjifyView.as_view())
]
