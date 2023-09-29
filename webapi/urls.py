from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, CommentViewSet, GameViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'games', GameViewSet)

urlpatterns = [
    path('', include(router.urls)),
]