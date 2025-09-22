from django.urls import path
from .views import PasswordCheckAPIView

urlpatterns = [
    path("check-password/", PasswordCheckAPIView.as_view(), name="check-password"),
]
