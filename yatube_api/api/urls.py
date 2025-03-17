from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api import views

router = DefaultRouter()
router.register(r"groups", views.GroupViewSet)
router.register(r"posts", views.PostViewSet)
router.register(
    r"posts/(?P<post_id>\d+)/comments", views.CommentViewSet, basename="posts"
)


urlpatterns = [
    path("", include(router.urls)),
]
