from django.urls import path
from .views import CookieStandList, CookieStandListDetail

urlpatterns = [
    path("", CookieStandList.as_view(), name="thing_list"),
    path("<int:pk>/", CookieStandListDetail.as_view(), name="thing_detail"),
]
