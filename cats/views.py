from .models import Cats
from .serializers import CatsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def CatsListView(request):
    serializer = CatsSerializer(Cats.objects.all(), many=True)
    return Response(serializer.data)


@api_view(["GET"])
def CatsDetailView(request, pk):
    serializer = CatsSerializer(Cats.objects.get(pk=pk))
    return Response(serializer.data)


@api_view(["POST"])
def CatsCreateView(request):
    serializer = CatsSerializer(data=request.data)
    serializer.is_valid()
    serializer.save()
    return Response(serializer.data)


@api_view(["PUT", "PATCH"])
def CatsUpdateView(request, pk):
    cat = Cats.objects.get(pk=pk)

    if request.method == "PUT":
        serializer = CatsSerializer(cat, data=request.data)

    if request.method == "PATCH":
        serializer = CatsSerializer(cat, data=request.data, partial=True)

    serializer.is_valid()
    serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def CatsDeleteView(request, pk):
    cat = Cats.objects.get(pk=pk)
    cat.delete()
    return Response({"message": "Deleted"})