from django.db import models
from datetime import datetime
from django.utils.timezone import now
from agents.models import Agent


class Properties(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'

    class PropertyType(models.TextChoices):
        PLOT = 'Plot'
        HOME = 'Home'
        SHOP = 'Shop'

    class HomeType (models.TextChoices):
        HOME = 'Home'
        FLAT = 'Flat'
        FORM_HOUSE = 'Form House'

    class PlotType (models.TextChoices):
        COMMERCIAL = 'Commercial'
        RESIDENTIAL = 'Residential'
        INDUSTRIAL = 'Industrial'
        AGRICULTURAL = 'Agricultural'

    class ShopType (models.TextChoices):
        MEDICAL_STORE = 'Medical Store'
        CLOTH_SHOP = 'Cloth Shop'
        COSMETICS_SHOP = 'Cosmetics Shop'
        GENERAL_STORE = 'General Store'
        MOBILE_SHOP = 'Mobile Shop'

    class AreaType(models.TextChoices):
        MARLA = 'Marla'
        KANAL = 'Kanal'
        SQFT = 'SQFT'

    class City (models.TextChoices):
        LAHORE = 'Lahore'
        ISLAMABAD = 'Islamabad'
        KARACHI = 'Karachi'
        MULTAN = 'Multan'

    class State (models.TextChoices):
        PUNJAB = 'Punjab'
        SINDH = 'Sindh'
        KPK = 'KPK'
        BALOCHISTAN = 'Balochistan'
    agent = models.ForeignKey(
        Agent, on_delete=models.DO_NOTHING, related_name='agentuser')
    slug = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=155)
    address = models.CharField(max_length=150)
    city = models.CharField(
        max_length=50, choices=City.choices, default=City.LAHORE)
    state = models.CharField(
        max_length=50, choices=State.choices, default=State.PUNJAB)
    description = models.TextField(blank=True)
    sale_type = models.CharField(
        max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE, blank=True)
    property_type = models.CharField(
        max_length=50, choices=PropertyType.choices,  blank=True)
    plot_type = models.CharField(
        max_length=50, choices=PlotType.choices,  blank=True)
    shop_type = models.CharField(
        max_length=50, choices=ShopType.choices,  blank=True)
    home_type = models.CharField(
        max_length=50, choices=HomeType.choices,  blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField(blank=True, null=True)
    bathrooms = models.IntegerField(blank=True, null=True)
    area_type = models.CharField(
        max_length=50, choices=AreaType.choices)
    area_size = models.IntegerField()
    main_image = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title
