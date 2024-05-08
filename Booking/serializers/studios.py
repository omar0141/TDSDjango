from rest_framework import serializers
from Booking.models.studios import Studios
from Booking.serializers.users import UserSerializer


class StudioSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Studios
        fields = ["id", "name", "maximum_daily_capacity", "user"]

    def create(self, validated_data):
        user = self.context["request"].user
        return Studios.objects.create(
            name=validated_data["name"],
            maximum_daily_capacity=validated_data["maximum_daily_capacity"],
            user=user,
        )
