from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/countries/', include('base.api.Countries.countries_urls')),
    path('api/login/', include('base.api.Login.login_urls')),
    path('api/airlines/', include('base.api.Airline_Companies.airline_companies_urls')),
]
