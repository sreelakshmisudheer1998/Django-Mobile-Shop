from django.urls import path, include
from .views import registration,index,login_view

urlpatterns = [
    path('cindex',index,name='cindex'),
    path("account", registration, name="account"),
    path("login", login_view, name="login"),
]
