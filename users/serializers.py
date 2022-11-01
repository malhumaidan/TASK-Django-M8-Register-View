from django.contrib.auth import get_user_model
from rest_framework import serializers

# Create your views here.

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name"]

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        new_user=User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data