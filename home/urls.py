from django.urls import path

from .views import GetToken
urlpatterns = [
    path('token/', GetToken.as_view(), name='token'),
]