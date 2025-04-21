from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer
from products.models import Product


# Create your views here.

def hello(request):
    print(request)
    # data = Product.objects.all()
    # d=data[0]
    # d.price=1500
    # d.save()

    return HttpResponse("Hello, world. You're at the polls page.")


@api_view(['GET','POST'])
def products(request):
    if request.method == 'GET':
        data=Product.objects.all()
        serialized_data  = ProductSerializer(data, many=True)
        return Response(serialized_data.data)
    elif request.method == 'POST':
        data=request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def product(request, id):
    try:
        data=Product.objects.get(pk=id)
        serialized_data = ProductSerializer(data)
        return Response(serialized_data.data)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

