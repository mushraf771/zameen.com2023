from django.urls import path
from .views import PropertiesView, PropertyView, PlotsSearchView, ShopsSearchView, SearchView, PropertiesHomesView, PropertiesPlotsView, PropertiesShopsView
urlpatterns = [
    path('', PropertiesView.as_view(), name='properties-view'),
    # path('addproperty', AddPropertyView.as_view(), name='add-property-view'),
    path('homes/', PropertiesHomesView.as_view(), name='properties-home-view'),
    path('plots/', PropertiesPlotsView.as_view(), name='properties-home-view'),
    path('shops/', PropertiesShopsView.as_view(), name='properties-home-view'),
    path('search/', SearchView.as_view(), name='search-view'),
    path('plotsearch/', PlotsSearchView.as_view(), name='plots-search-view'),
    path('shopsearch/', ShopsSearchView.as_view(), name='shops-search-view'),
    path('<slug>/', PropertyView.as_view(), name='property-view'),
]
