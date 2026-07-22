from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'first_name', 'last_name', 'phone_number', 'bio', 'cat_breed']
        read_only_fields = ['id']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            phone_number=validated_data["phone_number"],
            bio=validated_data.get("bio", ""),
            cat_breed=validated_data.get("cat_breed", ""),
            password=validated_data["password"],
        )
        return user