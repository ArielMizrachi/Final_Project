from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/countries/', include('base.api.Countries.countries_urls')),
    path('api/login/', include('base.api.Login.login_urls')),
    path('api/airlines/', include('base.api.Airline_Companies.airline_companies_urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
