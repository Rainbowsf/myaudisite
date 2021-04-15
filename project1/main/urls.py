from django.urls import path
from . import views

urlpatterns = [
    path('products', views.products, name="products"),
    path('e-tron', views.etron, name="e-tron"),
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contacts', views.contacts, name="contacts"),
    path('sitemap', views.sitemap, name="sitemap"),
]