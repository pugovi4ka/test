from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.auth.views import login
from mycatalog.views import catalog, product_page, edit

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mytest.views.home', name='home'),
                       # url(r'^mytest/', include('mytest.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', catalog, name='catalog'),
                       url(r'^product/(?P<id>\d+)/$', product_page, name='product_page'),
                       url(r'^edit/(?P<id>\d+)/$', edit, name='edit'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
