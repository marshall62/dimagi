from django.urls import path, include
from . import views

urlpatterns = [
    # path('',views.UserLocationView.as_view(), name='user-location'),
    path('users/',views.UserListView.as_view(), name='user-locations'),
    path('', views.UserFormView.as_view(), name='user-form')
]