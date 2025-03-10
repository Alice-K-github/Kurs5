from django.contrib import admin
from django.urls import path
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from users.views import CustomUserCreateAPIView, UserRetriveAPIView

app_name = 'users'

urlpatterns = [
                path("admin/", admin.site.urls),
                path('register/', CustomUserCreateAPIView.as_view(), name='register'),
                path('<int:pk>/', UserRetriveAPIView.as_view(), name='register'),

                path('token/', TokenObtainPairView.as_view(permission_classes=[AllowAny]), name='token'),
                path('token/refresh/', TokenRefreshView.as_view(permission_classes=[AllowAny]), name='token_refresh'),
        ]
