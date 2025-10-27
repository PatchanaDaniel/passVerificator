from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PasswordCheckSerializer
from .bloom_loader import BLOOM


class PasswordCheckAPIView(APIView):
    """
    Vérifie si le mot de passe est présent dans rockyou.txt
    password: mot de passe à vérifier
    example request:
    {
        "password": "1234"
    }
    """

    def post(self, request):
        serializer = PasswordCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data["password"]

        if password in BLOOM:
            return Response(
                {
                    "password": password,
                    "compromised": True,
                    "message": "⚠️ Mot de passe compromis !"
                },
                status=status.HTTP_200_OK)

        return Response(
            {
                "password": password,
                "compromised": False,
                "message": "✅ Mot de passe sûr"
            },
            status=status.HTTP_200_OK)
