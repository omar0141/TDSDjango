from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from Booking.models.reserves import Reserves
from Booking.serializers.reserves import ReserveSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import permission_required
from datetime import timedelta
from django.utils import timezone


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@permission_required("Booking.customer", raise_exception=True)
def create_reserve(request):
    try:
        reserve = ReserveSerializer(data=request.POST, context={"request": request})
        if reserve.is_valid():
            reserve.save()
            res = {
                "data": None,
                "message": "Your reserve has been successfully created.",
            }
            return Response(res, status=200)
        else:
            res = {
                "data": None,
                "message": reserve.errors,
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
@permission_required("Booking.customer", raise_exception=True)
def cancel_reserve(request, reserve_id):
    try:
        current_time = timezone.localtime(timezone.now()) + timedelta(hours=2)
        reserve = Reserves.objects.get(id=reserve_id)
        diff = (current_time - reserve.add_stamp).seconds / 60
        print(current_time)
        if diff < 15:
            Reserves.objects.filter(id=reserve_id).update(cancel=current_time)
            res = {
                "data": None,
                "message": "Your reserve has been canceled successfully.",
            }
            return Response(res, status=200)
        else:
            res = {
                "data": None,
                "message": "Sorry! You can't cancel your reserve after 15 minutes.",
            }
            return Response(res, status=400)
    except Exception as e:
        if type(e) is Reserves.DoesNotExist:
            res = {
                "data": None,
                "message": "Reserve not found.",
            }
            return Response(res, status=400)
        res = {
            "data": None,
            "message": str(e),
        }
        return Response(res, status=500)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@permission_required("Booking.owner", raise_exception=True)
def get_owner_resrves(request):
    try:
        reserves = Reserves.objects.select_related("studio", "customer").filter(
            studio__user_id=request.user.id, cancel=None
        )
        reserves = ReserveSerializer(reserves, many=True).data
        res = {
            "data": {"reserves": reserves},
            "message": None,
        }
        return Response(res, status=200)
    except Exception as e:
        res = {
            "data": None,
            "message": str(e),
        }
        return Response(res, status=500)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@permission_required("Booking.customer", raise_exception=True)
def get_customer_resrves(request):
    try:
        reserves = Reserves.objects.select_related("studio").filter(
            customer=request.user, cancel=None
        )
        reserves = ReserveSerializer(reserves, many=True).data
        res = {
            "data": {"reserves": reserves},
            "message": None,
        }
        return Response(res, status=200)
    except Exception as e:
        res = {
            "data": None,
            "message": str(e),
        }
        return Response(res, status=500)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@permission_required("Booking.admin", raise_exception=True)
def get_all_resrves(request):
    try:
        reserves = Reserves.objects.select_related("studio").filter(cancel=None)
        reserves = ReserveSerializer(reserves, many=True).data
        res = {
            "data": {"reserves": reserves},
            "message": None,
        }
        return Response(res, status=200)
    except Exception as e:
        res = {
            "data": None,
            "message": str(e),
        }
        return Response(res, status=500)
