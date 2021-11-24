from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CookieStand
from .permissions import IsOwnerOrReadOnly
from .serializers import Cookie_standSerializer


class CookieStandList(ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = Cookie_standSerializer


class CookieStandListDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = Cookie_standSerializer
