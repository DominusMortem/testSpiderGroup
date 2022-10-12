from django.contrib import admin
from django.urls import path
from django.urls.conf import include

api = [
    path('', include('users.urls', namespace='users')),
    path('', include('organizations.urls', namespace='organizations')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api)),
]
