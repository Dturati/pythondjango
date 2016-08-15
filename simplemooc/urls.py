"""simplemooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include,patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

#minhas urls
urlpatterns = [
    #url(r'^$', 'simplemooc.core.views.home', name='home'), #Caminho da view home
    #url(r'^$', 'simplemooc.core.views.contact', name='contact'), #Caminho da view home
    url(r'^', include('simplemooc.core.urls', namespace='core')), #Caminho da view home
    url(r'^conta/', include('simplemooc.accounts.urls', namespace='accounts')), #Caminho da view home
    url(r'^cursos/', include('simplemooc.courses.urls', namespace='index')), #Caminho da view homen NAMESPACE USADO NA VIEW
    url(r'^admin/', admin.site.urls),
]

#Para carregar imagem
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
