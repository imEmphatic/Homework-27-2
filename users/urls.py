from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    CustomTokenObtainPairView,
    PaymentListView,
    UserCreateView,
    UserProfileView,
)

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="user-register"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("payments/", PaymentListView.as_view(), name="payment-list"),
    path("users/<int:id>/", UserProfileView.as_view(), name="user-profile"),
]
