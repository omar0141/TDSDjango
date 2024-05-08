import rest_framework_filters as filters
from Booking.models.studios import Studios


class StudioFilter(filters.FilterSet):
    class Meta:
        model = Studios
        fields = {"name": ["startswith", "contains", "endswith"], "id": ["exact"]}
