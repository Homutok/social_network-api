from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from blog.views import BlogViewList, BlogViewDetail
from profiles.views import UserList, UserDetail, MyUserDetail
from post_likes.views import LikeViewSet
from post_comments.views import CommentViewSet

router = routers.DefaultRouter()

router.register(r'Likes', LikeViewSet)
router.register(r'Comments', CommentViewSet, basename='Comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/Blog/', BlogViewList.as_view()),
    path('api/Blog/<int:pk>/', BlogViewDetail.as_view()),
    path('api/Profile/', UserList.as_view()),
    path('api/Profile/<int:pk>/', UserDetail.as_view()),
    path('api/Myprofile/', MyUserDetail.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
