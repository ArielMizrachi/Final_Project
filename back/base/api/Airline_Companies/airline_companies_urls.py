from django.urls import path
from base.api.Airline_Companies import airline_companies_views
 
urlpatterns = [
    path('', airline_companies_views.GetRoutes),
    path('GetAirlines/', airline_companies_views.GetAirlines),
    path('GetAirlines/<id>', airline_companies_views.GetAirlines),
    path('AddAirline/', airline_companies_views.AddAirline),
    # path('DelCountries/<id>', airline_companies_views.DelCountries),
    # path('PutCountries/<id>', airline_companies_views.PutCountries),

    
]

