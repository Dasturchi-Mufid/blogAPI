from django.urls import path, include
from . import views


urlpatterns = [
    path('posts/',views.PostList.as_view()),
    path('auth/',include('rest_framework.urls'))
]
