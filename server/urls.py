from django.urls import path, include
from django.contrib import admin

admin.autodiscover()

import assistant.views


urlpatterns = [
    path("", assistant.views.index, name="index")
]