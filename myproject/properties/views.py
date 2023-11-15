from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework import permissions
from .models import Properties
from .serializers import PropertiesSerializer, ShopsSerializer, AddPropertySerializer, PropertiesDetailSerializer, PlotsSerializer
from datetime import datetime, timezone, timedelta
from accounts.models import UserAccount


class PropertiesView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Properties.objects.order_by(
        '-list_date').filter(is_published=True)
    serializer_class = PropertiesSerializer
    lookup_field = 'slug'

    def perform_create(self, serializer_class):
        serializer_class.save(agent=self.request.user)


class PropertiesHomesView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Properties.objects.order_by(
        '-list_date').filter(property_type='home', is_published=True)
    serializer_class = PropertiesSerializer
    lookup_field = 'slug'


class PropertiesPlotsView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Properties.objects.order_by(
        '-list_date').filter(property_type='plot', is_published=True)
    serializer_class = PropertiesSerializer
    lookup_field = 'slug'


class PropertiesShopsView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Properties.objects.order_by(
        '-list_date').filter(property_type='shops', is_published=True)
    serializer_class = PropertiesSerializer
    lookup_field = 'slug'


class PropertyView(RetrieveAPIView):
    # permission_classes = (permissions.AllowAny, )
    queryset = Properties.objects.order_by(
        '-list_date').filter(is_published=True)
    serializer_class = PropertiesDetailSerializer
    lookup_field = 'slug'


class PlotsSearchView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = PlotsSerializer

    def post(self, request, format=None):
        # order by is_published
        queryset = Properties.objects.order_by(
            '-list_date').filter(is_published=True, property_type='plot')
        data = self.request.data
        city = data['city']
        queryset = queryset.filter(city__iexact=city)
        # by state search
        state = data['state']
        queryset = queryset.filter(state__iexact=state)
# filter by price
        price = data['price']
        if price == '0+':
            price = 0
        elif price == '100,000+':
            price = 100000
        elif price == '200,000+':
            price = 200000
        elif price == '300,000+':
            price = 300000
        elif price == '400,000+':
            price = 400000
        elif price == '500,000+,':
            price = 500000
        elif price == '1,000,000+':
            price = 1000000
        elif price == '20,00,000+':
            price = 2000000
        elif price == 'Any':
            price = -1
        if price != -1:
            queryset = queryset.filter(price__gte=price)
        area_size = data['area_size']
        if area_size == '0':
            area_size = 0
        elif area_size == '1':
            area_size = 1
        elif area_size == '3':
            area_size = 3
        elif area_size == '5':
            area_size = 5
        elif area_size == '7':
            area_size = 7
        elif area_size == '9':
            area_size = 9
        elif area_size == '10':
            area_size = 10
        elif area_size == '20':
            area_size = 20
        elif area_size == 'Any':
            area_size = -1
        if area_size != -1:
            queryset = queryset.filter(area_size__iexact=area_size)

        serializer = PlotsSerializer(queryset, many=True)
        print(serializer)
        return Response(serializer.data)


class ShopsSearchView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ShopsSerializer

    def post(self, request, format=None):
        # order by is_published
        queryset = Properties.objects.order_by(
            '-list_date').filter(is_published=True, property_type='shop')
        data = self.request.data
        city = data['city']
        queryset = queryset.filter(city__iexact=city)
        sale_type = data['sale_type']
        queryset = queryset.filter(sale_type__iexact=sale_type)
        shop_type = data['shop_type']
        queryset = queryset.filter(shop_type__iexact=shop_type)
        # by state search
        state = data['state']
        queryset = queryset.filter(state__iexact=state)
# filter by price
        price = data['price']
        if price == '0+':
            price = 0
        elif price == '100,000+':
            price = 100000
        elif price == '200,000+':
            price = 200000
        elif price == '300,000+':
            price = 300000
        elif price == '400,000+':
            price = 400000
        elif price == '500,000+,':
            price = 500000
        elif price == '1,000,000+':
            price = 1000000
        elif price == '20,00,000+':
            price = 2000000
        elif price == 'Any':
            price = -1
        if price != -1:
            queryset = queryset.filter(price__gte=price)
        queryset = queryset.filter(price__gte=price)
# areA SIZE
        area_size = data['area_size']
        if area_size == '0':
            area_size = 0
        elif area_size == '1':
            area_size = 1
        elif area_size == '3':
            area_size = 3
        elif area_size == '5':
            area_size = 5
        elif area_size == '7':
            area_size = 7
        elif area_size == '9':
            area_size = 9
        elif area_size == '10':
            area_size = 10
        elif area_size == '20':
            area_size = 20
        elif area_size == 'Any':
            area_size = -1
        if area_size != -1:
            queryset = queryset.filter(area_size__iexact=area_size)

        serializer = ShopsSerializer(queryset, many=True)
        print(serializer)
        return Response(serializer.data)


class SearchView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = PropertiesSerializer
    def post(self, request, format=None):
        # order by is_published
        queryset = Properties.objects.order_by(
            '-list_date').filter(is_published=True)
        data = self.request.data
        # sale type filter
        sale_type = data['sale_type']
        queryset = queryset.filter(sale_type__iexact=sale_type)
        # city search
        city = data['city']
        queryset = queryset.filter(city__iexact=city)
        # by state search
        state = data['state']
        queryset = queryset.filter(state__iexact=state)
# filter by price
        price = data['price']
        if price == '0+':
            price = 0
        elif price == '100,000+':
            price = 100000
        elif price == '200,000+':
            price = 200000
        elif price == '300,000+':
            price = 300000
        elif price == '400,000+':
            price = 400000
        elif price == '500,000+,':
            price = 500000
        elif price == '1,000,000+':
            price = 1000000
        elif price == '20,00,000+':
            price = 2000000
        elif price == 'Any':
            price = -1
        if price != -1:
            queryset = queryset.filter(price__gte=price)

# bedrooms search
        bedrooms = data['bedrooms']
        if bedrooms == '0+':
            bedrooms = 0
        elif bedrooms == '1+':
            bedrooms = 1
        elif bedrooms == '2+':
            bedrooms = 2
        elif bedrooms == '3+':
            bedrooms = 3
        elif bedrooms == '4+':
            bedrooms = 4
        elif bedrooms == '5+':
            bedrooms = 5
        elif bedrooms == '6+':
            bedrooms = 6
        queryset = queryset.filter(bedrooms__gte=bedrooms)
# home type search
        home_type = data['home_type']
        queryset = queryset.filter(home_type__iexact=home_type)
# bathrooms search
        bathrooms = data['bathrooms']
        if bathrooms == '0+':
            bathrooms = 1
        elif bathrooms == '1+':
            bathrooms = 1
        elif bathrooms == '2+':
            bathrooms = 2
        elif bathrooms == '3+':
            bathrooms = 3
        elif bathrooms == '4+':
            bathrooms = 4
        elif bathrooms == '5+':
            bathrooms = 5
        elif bathrooms == '6+':
            bathrooms = 6
        elif price == 'Any':
            price = -1
        if price != -1:
            queryset = queryset.filter(price__gte=price)
        queryset = queryset.filter(bathrooms__gte=bathrooms)
# home type search
        home_type = data['home_type']
        queryset = queryset.filter(home_type__iexact=home_type)
# search by Area Size
        area_size = data['area_size']
        if area_size == '0':
            area_size = 0
        elif area_size == '1':
            area_size = 1
        elif area_size == '3':
            area_size = 3
        elif area_size == '5':
            area_size = 5
        elif area_size == '7':
            area_size = 7
        elif area_size == '9':
            area_size = 9
        elif area_size == '10':
            area_size = 10
        elif area_size == '20':
            area_size = 20
        elif area_size == 'Any':
            area_size = -1
        if area_size != -1:
            queryset = queryset.filter(area_size__gte=area_size)
        queryset = queryset.filter(area_size__iexact=area_size)
# by keywords search in description
        keywords = data['keywords']
        queryset = queryset.filter(description__icontains=keywords)
# serializer data
        serializer = PropertiesSerializer(queryset, many=True)
        print(serializer)
        return Response(serializer.data)
