from django.urls import path
from .views import LoginView, LogoutView, CustomTokenRefreshView, RevokeTokenView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('token/revoke/', RevokeTokenView.as_view(), name='token_revoke'),
]
