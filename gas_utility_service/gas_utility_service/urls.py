from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from gas_utility_service import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("consumer_services.urls")),
]