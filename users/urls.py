from django.urls import path
from .views import HelloView, RegisterApiView

urlpatterns = [
        path('hello/', HelloView.as_view(), name='hello'),
        path('register/', RegisterApiView.as_view(), name='register'),
        # path('login/', LoginUserApiView.as_view(), name='login'),
]
