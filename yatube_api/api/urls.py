from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, CommentsViewSet, GroupViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>[\d]+)/comments',
    CommentsViewSet,
    basename='comment',
)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
