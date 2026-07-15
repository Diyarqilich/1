from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView


from .models import Cat
from .serializers import CatSerializer


class CatListViewSet(ListAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatCreateViewSet(CreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatRetrieveViewSet(RetrieveAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatUpdateViewSet(UpdateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatDestroyViewSet(DestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatRetrieveUpdateDestroyViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer