from django.urls import path
from .views import SendTelegramMessage

urlpatterns = [
    path("telegram/send/", SendTelegramMessage.as_view(), name="telegram-send"),
]
