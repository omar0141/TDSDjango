from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import Permission
from Booking.models.custom_user_permissions import CustomUserPermissions


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=False,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    first_name = serializers.CharField(
        max_length=10,
        validators=[MinLengthValidator(3)],
        required=True,
    )
    last_name = serializers.CharField(
        max_length=10,
        validators=[MinLengthValidator(3)],
        required=True,
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        write_only=True,
        max_length=20,
        validators=[MinLengthValidator(6)],
    )
    type = serializers.ChoiceField(
        required=False,
        choices=CustomUserPermissions._meta.permissions,
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password", "type"]

    def create(self, validated_data):
        if "type" not in validated_data:
            raise serializers.ValidationError("`type` is a required field.")

        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["email"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        permission = permission = Permission.objects.get(
            codename=validated_data["type"]
        )
        user.user_permissions.add(permission)
        return user

    def update(self, instance, validated_data):
        user = User.objects.filter(id=instance.id).update(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["email"],
            email=validated_data["email"],
        )
        return user
