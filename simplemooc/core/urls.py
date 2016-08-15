from django.conf.urls import url,include,patterns

#minhas urls
urlpatterns = [
    url(r'^$', 'simplemooc.core.views.home', name='home'), #Caminho da view home
    url(r'^contato/$', 'simplemooc.core.views.contact', name='contact'), #Caminho da view home
]