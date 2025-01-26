from django.urls import path

from .views import PaymentListView, UserProfileView, UserUpdateView

urlpatterns = [
    path("payments/", PaymentListView.as_view(), name="payment-list"),
    path("users/<int:id>/update/", UserUpdateView.as_view(), name="user-update"),
    path("users/<int:id>/profile/", UserProfileView.as_view(), name="user-profile"),
]
