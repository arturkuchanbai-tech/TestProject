from django.contrib import admin
from django.urls import path, include  # include нужен, чтобы подключить urls из приложения

urlpatterns = [
    path('admin/', admin.site.urls),       
    path('api/v1/studis/', include('Manage.urls')), 
]
# свагер