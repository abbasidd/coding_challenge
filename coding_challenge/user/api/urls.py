from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,Deposits_view
router = DefaultRouter()
router.register(r'user', UserViewSet, basename='account')

urlpatterns = [
    path('', include(router.urls)),
    path("deposit/", Deposits_view.as_view()),
    path("get-deposit/", Deposits_view.as_view()),
    path("get-deposit/<int:id>/", Deposits_view.as_view()),
]