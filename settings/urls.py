"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fundacion/', include('fundacion.urls', namespace='fundacion')),
    path('', include('asilo.urls', namespace='asilo')),
    path('usuarios/', include('usuarios.urls', namespace="usuarios")),
    path('contabilidad/',include('contabilidad.urls', namespace="contabilidad")),
    path('reportes/', include('reportes.urls', namespace="reportes")),
    path('api-auth/', include('rest_framework.urls'))
] 
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
