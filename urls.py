from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ublog.posts.views',

    (r'^$', 'index'),
    (r'^dashboard/$', 'dashboard'),
    (r'^profile/$', 'profile'),

    (r'^post/$', 'add_post'),
    (r'^post/(?P<post_id>\d+)/$', 'get_post'),

    (r'^login/$',  'login'),
    (r'^logout/$', 'logout'),

    # Example:
    # (r'^ublog/', include('ublog.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns("django.views",
        url(r"^static/(?P<path>.*)", "static.serve", {
            "document_root": '/home/pmandes/Devel/projects/ublog/static/',
        })
    )
