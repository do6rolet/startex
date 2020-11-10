from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet

router = routers.DefaultRouter()
router.register('product_list', ProductViewSet)
# router.register('ratings', RatingViewSet)
# router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
