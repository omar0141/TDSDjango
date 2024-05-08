from rest_framework import serializers
from Booking.models.reserves import Reserves
from Booking.models.studios import Studios
from Booking.serializers.studios import StudioSerializer
from Booking.serializers.users import UserSerializer


class ReserveSerializer(serializers.ModelSerializer):
    studio = StudioSerializer(required=False)
    customer = UserSerializer(required=False)
    id = serializers.IntegerField(required=False)
    add_stamp = serializers.DateTimeField(required=False)
    studio_id = serializers.IntegerField()

    class Meta:
        model = Reserves
        fields = [
            "id",
            "from_date",
            "to_date",
            "studio",
            "customer",
            "studio_id",
            "add_stamp",
        ]

    def create(self, validated_data):
        user = self.context["request"].user
        from_date = validated_data["from_date"]
        to_date = validated_data["to_date"]
        studio_id = validated_data["studio_id"]
        if from_date > to_date:
            raise Exception("`from_date` must be less than `to_date`.")
        studio = Studios.objects.get(id=studio_id)
        diff = (to_date - from_date).days
        if diff > studio.maximum_daily_capacity:
            raise Exception(
                f"difference between `from_date` and `to_date` must be less than {studio.maximum_daily_capacity} days."
            )
        return Reserves.objects.create(
            from_date=from_date,
            to_date=to_date,
            studio_id=studio_id,
            customer=user,
        )
