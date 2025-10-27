from rest_framework import serializers


class PasswordCheckSerializer(serializers.Serializer):
    """Serializer for password checking.
    """
    password = serializers.CharField(write_only=True)
