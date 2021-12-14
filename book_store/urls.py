from django.contrib import admin
from django.urls import path, include

urlpatterns = [
        #Djando admin
    path('admin/', admin.site.urls),
        #User Management
    path('accounts/', include('allauth.urls')),
        #Local apps
    path('', include('pages.urls')),
]
