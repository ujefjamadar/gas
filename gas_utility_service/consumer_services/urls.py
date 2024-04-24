from django.urls import path
from consumer_services import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.home),
    path('',views.user_login, name='login'),
    path('servicepage/',views.view_service_requests),
    path('req',views.submit_service_request,name='sr'),
    path('logout/',views.user_logout),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
