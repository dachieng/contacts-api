from django.urls import path

from users import views

urlpatterns = [
    path('auth/', views.AuthUserView.as_view(), name="register"),
    path('login/', views.LoginUserView.as_view(), name='login')
]