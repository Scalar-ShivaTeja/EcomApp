from symtable import Class

from rest_framework import serializers

from .models import User,Address,ShippingAddress



class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'

class CreateShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ['street','city','state','zipcode','country']

class UserSerializer(serializers.ModelSerializer):
    shipping_addresses = ShippingAddressSerializer(many=True,read_only=True)
    default_shipping_address = ShippingAddressSerializer(read_only=True)
    class Meta:
        model = User
        fields = '__all__'
