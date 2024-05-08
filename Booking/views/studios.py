from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from Booking.filters.studios import StudioFilter
from Booking.models.studios import Studios
from Booking.serializers.studios import StudioSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import permission_required


@api_view(["GET"])
def get_studios(request):
    try:
        studios = Studios.objects.all()
        filterset = StudioFilter(request.GET, queryset=studios)
        studios = StudioSerializer(filterset.qs, many=True).data
        res = {
            "data": {"studios": studios},
            "message": None,
        }
        return Response(res, status=200)
    except Exception as e:
        res = {
            "data": None,
            "message": str(e),
        }
        return Response(res, status=500)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@permission_required("Booking.owner", raise_exception=True)
def create_studio(request):
    try:
        studio = StudioSerializer(data=request.POST, context={"request": request})
        if studio.is_valid():
            studio.save()
            res = {
                "data": None,
                "message": "Your studio has been successfully created.",
            }
            return Response(res, status=200)
        else:
            res = {
                "data": None,
                "message": studio.errors,
            }
            return Response(res, status=400)
    except Exception as e:
        res = {
            "data": None,
            "message": str(e),
        }
        return Response(res, status=500)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
@permission_required("Booking.owner", raise_exception=True)
def update_studio(request, studio_id):
    try:
        studio = Studios.objects.get(id=studio_id)
        studio = StudioSerializer(studio, data=request.POST, partial=True)
        if studio.is_valid():
            studio.save()
            res = {
                "data": None,
                "message": "Your studio has been successfully updated.",
            }
            return Response(res, status=200)
        else:
            res = {
                "data": None,
                "message": studio.errors,
            }
            return Response(res, status=400)
    except Exception as e:
        if type(e) is Studios.DoesNotExist:
            res = {
                "data": None,
                "message": "Studio not found.",
            }
            return Response(res, status=400)
        res = {
            "data": None,
            "message": str(e),
        }
        return Response(res, status=500)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
@permission_required("Booking.owner", raise_exception=True)
def delete_studio(request, studio_id):
    try:
        Studios.objects.get(id=studio_id)
        Studios.objects.filter(id=studio_id).delete()
        res = {
            "data": None,
            "message": "Your studio has been successfully deleted.",
        }
        return Response(res, status=200)
    except Exception as e:
        if type(e) is Studios.DoesNotExist:
            res = {
                "data": None,
                "message": "Studio not found.",
            }
            return Response(res, status=400)
        res = {
            "data": None,
            "message": str(e),
        }
        return Response(res, status=500)
