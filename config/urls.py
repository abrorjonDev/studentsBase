from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from bot.webhook import webhook


urlpatterns = [
    path('webhook/', csrf_exempt(webhook), name='webhook'),
    path('admin/', admin.site.urls),

]
