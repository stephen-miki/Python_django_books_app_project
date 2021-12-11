from django.contrib import admin
from django.urls import path, include

urlpatterns = [
        #Djando admin
    path('admin/', admin.site.urls),
        #User Management
    path('accounts', include('django.contrib.auth.urls')),
        #Local apps
    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
]
