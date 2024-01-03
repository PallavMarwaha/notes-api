from rest_framework import serializers
from django.contrib.auth import password_validation, get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        Overrides create method to hash user password
        """

        user = User(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user
