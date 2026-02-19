import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SendTelegramMessage(APIView):
    def post(self, request):
        text = request.data.get("text", "").strip()
        if not text:
            return Response({"error": "text is required"}, status=status.HTTP_400_BAD_REQUEST)

        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"

        r = requests.post(
            url,
            json={"chat_id": settings.TELEGRAM_CHAT_ID, "text": text},
            timeout=10
        )

        data = r.json()
        if not data.get("ok"):
            return Response({"error": "Telegram error", "details": data}, status=status.HTTP_502_BAD_GATEWAY)

        return Response({"success": True}, status=status.HTTP_200_OK)
