from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('user/', include('django.contrib.auth.urls')),
    path('user/register', views.register, name='register'),
    path('delete/<int:note_id>', views.delete, name='delete')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
