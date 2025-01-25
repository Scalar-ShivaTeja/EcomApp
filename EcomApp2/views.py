import __future__ as request

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.response import responses, Response
from rest_framework.views import APIView

from .models import User,Address,ShippingAddress
from .serializers import UserSerializer,ShippingAddressSerializer,CreateShippingAddressSerializer

class UserListCreateAPIView(APIView):

    def get(self,request):
        users=User.objects.all().prefetch_related('shipping_addresses')
        return Response(UserSerializer(users,many=True).data)

    def post(self,request):
        serialzed_data=UserSerializer(data=request.data)
        if not serialzed_data.is_valid():
            return Response(serialzed_data.errors, status=status.HTTP_400_BAD_REQUEST)
        serialzed_data.save()
        return Response(serialzed_data.data, status=status.HTTP_201_CREATED)
class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShippingAddressListCreateAPIView(APIView):
    serializer_class = CreateShippingAddressSerializer

    def post(self,request,user_id):

        user=get_object_or_404(User, pk=user_id)
        serialzed_data=CreateShippingAddressSerializer(data=request.data)
        if not serialzed_data.is_valid():
            return Response(serialzed_data.errors, status=status.HTTP_400_BAD_REQUEST)

        shipping_address=ShippingAddress.objects.create(
            street=serialzed_data.data['street'],
            city=serialzed_data.validated_data.get('city'),
            state=serialzed_data.validated_data.get('state'),
            zipcode=serialzed_data.validated_data.get('zipcode'),
            country=serialzed_data.validated_data.get('country'),
            user=user
        )

        shipping_address.save()

        return Response(ShippingAddressSerializer(shipping_address).data, status=status.HTTP_201_CREATED)

class ShippinGAddressRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer