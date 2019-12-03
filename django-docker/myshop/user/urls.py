# coding=utf-8
from django.urls import path
from user.views import RegisterView, ActiveView, LoginView, LogoutView, UserInfoView, UserOrderView, AddressView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('active/<token>', ActiveView.as_view(), name='detail'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    # --------用户中心----------
    path('', UserInfoView.as_view(), name='user'),
    path('order/<page>', UserOrderView.as_view(), name='order'),
    path('address/', AddressView.as_view(), name='address'),
]
