from django.urls import URLPattern, path, include
from .views import SnackListView
urlpatterns = [
    path('', SnackListView.as_view(), name="snack_list")
]
