from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from Booking.serializers.users import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


@api_view(["POST"])
def login(request):
    try:
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            res = {
                "data": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user": UserSerializer(user).data,
                    "type": user.get_user_permissions(),
                },
                "message": "Login success.",
            }
            return Response(res, status=200)
        else:
            res = {
                "data": None,
                "message": "Invalid credentials",
            }
            return Response(res, status=401)
    except Exception as e:
        res = {
            "data": None,
            "message": str(e),
        }
        return Response(res, status=500)


@api_view(["POST"])
def register(request):
    try:
        user = UserSerializer(data=request.POST)
        if user.is_valid():
            user.save()
            res = {
                "data": None,
                "message": "Congratulations! Your account has been successfully created.",
            }
            return Response(res, status=200)
        else:
            res = {
                "data": None,
                "message": user.errors,
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
def update_user(request):
    try:
        user = User.objects.get(id=request.user.id)
        user = UserSerializer(user, data=request.data, partial=True)
        if user.is_valid():
            user.save()
            res = {
                "data": None,
                "message": "Your user has been successfully updated.",
            }
            return Response(res, status=200)
        else:
            res = {
                "data": None,
                "message": user.errors,
            }
            return Response(res, status=400)
    except Exception as e:
        if type(e) is User.DoesNotExist:
            res = {
                "data": None,
                "message": "User not found.",
            }
            return Response(res, status=400)
        res = {
            "data": None,
            "message": str(e),
        }
        return Response(res, status=500)
