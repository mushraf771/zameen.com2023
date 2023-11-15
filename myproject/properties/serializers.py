from rest_framework import serializers
from .models import Properties
from accounts.models import UserAccount
class PlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = ('city', 'state',
                 'area_type', 'area_size', 'price','plot_type','main_image','slug'
                  )
class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = ('city', 'state',
                 'area_type', 'area_size', 'price','sale_type','shop_type'
                  , 'title', 'address', 'slug', 'main_image'
                  )
class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = ('agent','title','slug','address','city','state','sale_type',
                  'home_type','bedrooms','bathrooms','area_type','area_size','price',
                  'main_image')
        # depth = 2
class PropertiesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = '__all__'
        lookup_field = 'slug'
        # depth=2
class AddPropertySerializer(serializers.ModelSerializer):
    agentuser =  PropertiesSerializer(read_only=True , many=True)
    class Meta:
        model = Properties
        # fields ='__all__'
        exclude =('main_image',)