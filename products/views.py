from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from products.serializers import ProductSerializer
from products.models import Product

#TODO : Resolve => DRF form issue => want to see field wise option to input data in post request
# from rest_framework.decorators import renderer_classes
# from rest_framework.renderers import BrowsableAPIRenderer

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
        products=Product.objects.all()

        name = request.GET.get('name')
        price = request.GET.get('price')
        description = request.GET.get('description')

        if name:
            products = products.filter(name__icontains=name)
        if price:
            products = products.filter(price=price)
        if description:
            products = products.filter(description__icontains=description)

        serialized_products  = ProductSerializer(products, many=True)
        return Response(serialized_products.data)
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
        product=Product.objects.get(pk=id)
        serialized_data = ProductSerializer(product)
        return Response(product.data)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

