from rest_framework.routers import SimpleRouter
from django.urls import include, path
from rest_framework.authtoken import views

from api.views import PostViewSet, GroupViewSet, CommentViewSet

router = SimpleRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment'
)


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
