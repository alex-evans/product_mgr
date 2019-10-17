from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('business_features/', include('business_features.urls')),
    path('admin/', admin.site.urls),
]
