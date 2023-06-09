from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('item.urls')),
    path('core/', include('core.urls')),
    path('users/', include('users.urls')),
]

#creating url for our static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
