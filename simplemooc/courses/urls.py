from django.conf.urls import url,include,patterns

#minhas urls
urlpatterns = patterns('simplemooc.courses.views',
                url(r'^$', 'index', name='index'),  # Caminho da view home
                #url(r'^(?P<pk>\d+)/$', 'simplemooc.courses.views.details', name='details'),  # Caminho da view home
                #url(r'^(?P<slug>[\w_-]+)/$', 'details', name='details'),  # Caminho da view home
                url(r'^(?P<slug>[\w_-]+)/$', 'details', name='details'),  # Caminho da view home
                url(r'^(?P<slug>[\w_-]+)/inscricao/$', 'enrollment', name='enrollment'),  # Caminho da view home
    )
