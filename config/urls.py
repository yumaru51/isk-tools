from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('isk_tools/quality_change_management/', include('quality_change_management.urls')),
]
