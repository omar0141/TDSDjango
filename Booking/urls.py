from django.urls import path
from .views.users import register, login, update_user
from .views.studios import create_studio, update_studio, delete_studio, get_studios
from .views.reserves import (
    create_reserve,
    cancel_reserve,
    get_owner_resrves,
    get_customer_resrves,
    get_all_resrves,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path("token/create", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify", TokenVerifyView.as_view(), name="token_verify"),
    path("login", login),
    path("register", register),
    path("user/update", update_user),
    path("studios/get", get_studios),
    path("studios/create", create_studio),
    path("studios/update/<int:studio_id>", update_studio),
    path("studios/delete/<int:studio_id>", delete_studio),
    path("reserves/create", create_reserve),
    path("reserves/cancel/<int:reserve_id>", cancel_reserve),
    path("reserves/owner/get", get_owner_resrves),
    path("reserves/customer/get", get_customer_resrves),
    path("reserves/admin/get", get_all_resrves),
]
